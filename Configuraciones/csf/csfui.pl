#!/usr/bin/perl
###############################################################################
# Copyright 2006-2016, Way to the Web Limited
# URL: http://www.configserver.com
# Email: sales@waytotheweb.com
###############################################################################
# start main
#use strict;
use lib '/usr/local/csf/lib';
use Fcntl qw(:DEFAULT :flock);
use File::Basename;
use Net::CIDR::Lite;
use IPC::Open3;
use ConfigServer::Config;
use ConfigServer::CheckIP;
use ConfigServer::Ports;
use ConfigServer::URLGet;
use ConfigServer::Sanity;
use ConfigServer::ServerCheck;
use ConfigServer::ServerStats;
use ConfigServer::Service;
use ConfigServer::RBLCheck;

umask(0177);

our ($chart, $ipscidr6, $ipv6reg, $ipv4reg, %config, %ips, $mobile,
     $urlget);

$ipscidr6 = Net::CIDR::Lite->new;

my $thisui = $config{THIS_UI};
my $config = ConfigServer::Config->loadconfig();
%config = $config->config;
$config{THIS_UI} = $thisui;

$ipv4reg = $config->ipv4reg;
$ipv6reg = $config->ipv6reg;

$mobile = 0;
if ($FORM{mobi}) {$mobile = 1}

$chart = 1;
if ($config{ST_ENABLE}) {
	if (!defined ConfigServer::ServerStats::init()) {$chart = 0}
}

print <<EOF;

<style type="text/css">
a {
	color: #000000;
	text-decoration: underline;
}
td {
	font-family:Arial, Helvetica, sans-serif;
	font-size:small;
}
body {
	font-family:Arial, Helvetica, sans-serif;
	font-size:small;
}
pre {
	font-family: Courier New, Courier;
	font-size: 12px;
}
.comment {
	border-radius:5px;
	border: 1px solid #DDDDDD;
	padding: 10px;
	font-family: Courier New, Courier;
	font-size: 14px
}
.value-default {
	background:#F5F5F5;
	padding:2px;
	border-radius:5px;
}
.value-other {
	background:#F4F4EA;
	padding:2px;
	border-radius:5px;
}
.value-disabled {
	background:#F5F5F5;
	padding:2px;
	border-radius:5px;
}
.value-warning {
	background:#FFC0CB;
	padding:2px;
	border-radius:5px;
}
.section {
	border-radius:5px;
	border: 2px solid #990000;
	padding: 10px;
	font-size:16px;
	font-weight:bold;
}
EOF
unless (-e "/etc/csuibuttondisable") {
	print <<EOF;
.input {
	min-width:0px;
	padding:3px;
	background:#FFFFFF;
	border-radius:3px;
	border:1px solid #A6C150;
	color:#990000 !important;
	font-family:Verdana, Geneva, sans-serif;
	text-shadow: 0px 1px 1px #CDCDCD;
	font-size:13px;
	font-weight:normal;
	margin:2px;
}
.input:hover {
	cursor:pointer;
	border:1px solid #A6C150;
	box-shadow: 0px 0px 6px 1px #A6C150;
}
input[type=text], textarea, select {
	-webkit-transition: all 0.30s ease-in-out;
	-moz-transition: all 0.30s ease-in-out;
	-ms-transition: all 0.30s ease-in-out;
	-o-transition: all 0.30s ease-in-out;
	transition: all 0.30s ease-in-out;
	border-radius:3px;
	outline: none;
	padding: 3px 0px 3px 3px;
	margin: 5px 1px 3px 0px;
	border: 1px solid #DDDDDD;
}
input[type=text]:focus, textarea:focus, select:focus {
	box-shadow: 0 0 5px #CC0000;
	padding: 3px 0px 3px 3px;
	margin: 5px 1px 3px 0px;
	border: 1px solid #CC0000;
}
EOF
}
print "</style>\n";

$urlget = ConfigServer::URLGet->new($config{URLGET}, "csf/$myv");
unless (defined $urlget) {
	$config{URLGET} = 1;
	$urlget = ConfigServer::URLGet->new($config{URLGET}, "csf/$version");
	print "<p>*WARNING* URLGET set to use LWP but perl module is not installed, reverting to HTTP::Tiny<p>\n";
}

if ($config{RESTRICT_UI} == 2) {
	print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr bgcolor='#FFFFFF'><td align='center'><font color='red'>csf UI Disabled via the RESTRICT_UI option in /etc/csf/csf.conf</font></td></tr>\n";
	print "</tr></table><br>\n";
	exit;
}

if ($FORM{ip} ne "") {$FORM{ip} =~ s/(^\s+)|(\s+$)//g}

if (($FORM{ip} ne "") and ($FORM{ip} ne "all") and (!checkip(\$FORM{ip}))) {
	print "[$FORM{ip}] is not a valid IP/CIDR";
}
elsif (($FORM{ignorefile} ne "") and ($FORM{ignorefile} =~ /[^\w\.]/)) {
	print "[$FORM{ignorefile}] is not a valid file";
}
elsif (($FORM{template} ne "") and ($FORM{template} =~ /[^\w\.]/)) {
	print "[$FORM{template}] is not a valid file";
}
elsif ($FORM{action} eq "lfdstatus") {
	print "<p>Show lfd status...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	ConfigServer::Service::statuslfd();
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "ms_list") {
	&modsec;
}
elsif ($FORM{action} eq "chart") {
	&chart;
}
elsif ($FORM{action} eq "systemstats") {
	&systemstats($FORM{graph});
}
elsif ($FORM{action} eq "ms_config") {
	sysopen (IN, "/usr/local/apache/conf/$FORM{template}", O_RDWR | O_CREAT) or die "Unable to open file: $!";
	flock (IN, LOCK_SH);
	my @confdata = <IN>;
	close (IN);
	chomp @confdata;

	print "<form action='$script' method='post'>\n";
	print "<input type='hidden' name='action' value='savems_config'>\n";
	print "<input type='hidden' name='template' value='$FORM{template}'>\n";
	print "<fieldset><legend><b>Edit $FORM{template}</b></legend>\n";
	print "<table align='center'>\n";
	print "<tr><td><textarea name='formdata' cols='80' rows='40' style='font-family: Courier New, Courier; font-size: 12px' wrap='off'>\n";
	foreach my $line (@confdata) {
		$line =~ s/\&/\&amp\;/g;
		$line =~ s/>/\&gt\;/g;
		$line =~ s/</\&lt\;/g;
		print $line."\n";
	}
	print "</textarea></td></tr></table></fieldset>\n";
	print "<p align='center'><input type='submit' class='input' value='Change'></p>\n";
	print "</form>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "savems_config") {
	$FORM{formdata} =~ s/\r//g;
	sysopen (OUT, "/usr/local/apache/conf/$FORM{template}", O_WRONLY | O_CREAT) or die "Unable to open file: $!";
	flock (OUT, LOCK_EX);
	seek (OUT, 0, 0);
	truncate (OUT, 0);
	if ($FORM{formdata} !~ /\n$/) {$FORM{formdata} .= "\n"}
	print OUT $FORM{formdata};
	close (OUT);

	print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><th align='left'>ModSecurity save $FORM{template}</th></tr>";
	print "<tr bgcolor='#F4F4EA'><td>You should restart Apache having changed this file</td></tr>\n";
	print "</table>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "lfdstart") {
	print "<p>Starting lfd...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	ConfigServer::Service::startlfd();
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "lfdrestart") {
	if ($config{DIRECTADMIN} or $config{THIS_UI}) {
		print "<p>Signal lfd to <i>restart</i>...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
		sysopen (OUT, "/var/lib/csf/lfd.restart",, O_WRONLY | O_CREAT) or die "Unable to open file: $!";
		close (OUT);
	} else {
		print "<p>Restarting lfd...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
		ConfigServer::Service::restartlfd();
	}
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "lfdstop") {
	print "<p>Stopping lfd...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	ConfigServer::Service::stoplfd();
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "status") {
	print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><td><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-l");
	if ($config{IPV6}) {
		print "\n\nip6tables:\n\n";
		&printcmd("/usr/sbin/csf","-l6");
	}
	print "</pre></td></tr></table>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "start") {
	print "<p>Starting csf...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-sf");
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "restart") {
	print "<p>Restarting csf...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-sf");
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "restartq") {
	print "<p>Restarting csf via lfd...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-q");
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "temp") {
	my $class = '#F4F4EA';
	print "<table align='center' border='0' cellspacing='0' cellpadding='4' bgcolor='FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><th>&nbsp;</th><th>A/D</th><th>IP address</th><th>Port</th><th>Dir</th><th>Time To Live</th><th>Comment</th></tr>\n";
	my @deny;
	if (! -z "/var/lib/csf/csf.tempban") {
		open (IN, "</var/lib/csf/csf.tempban") or die $!;
		@deny = <IN>;
		chomp @deny;
		close (IN);
	}
	foreach my $line (reverse @deny) {
		if ($line eq "") {next}
		my ($time,$ip,$port,$inout,$timeout,$message) = split(/\|/,$line);
		$time = $timeout - (time - $time);
		if ($port eq "") {$port = "*"}
		if ($inout eq "") {$inout = " *"}
		if ($time < 1) {
			$time = "<1";
		} else {
			my $days = int($time/(24*60*60));
			my $hours = ($time/(60*60))%24;
			my $mins = ($time/60)%60;
			my $secs = $time%60;
			$days = $days < 1 ? '' : $days .'d ';
			$hours = $hours < 1 ? '' : $hours .'h ';
			$mins = $mins < 1 ? '' : $mins . 'm ';
			$time = $days . $hours . $mins . $secs . 's'; 
		}
		print "<tr bgcolor='$class'><td>&nbsp;<a href='$script?action=temprm&ip=$ip'><img src='$images/delete.png' border='0' alt='Unblock $ip?'></a>&nbsp;<a href='$script?action=temptoperm&ip=$ip'><img src='$images/perm.png' border='0' alt='Permanently $ip?'></a>&nbsp;</td><td>DENY</td><td>$ip</td><td>$port</td><td>$inout</td><td>$time</td><td>$message</td></tr>\n";
		if ($class eq '#FFFFFF') {$class = '#F4F4EA'} else {$class = '#FFFFFF'}
	}
	my @allow;
	if (! -z "/var/lib/csf/csf.tempallow") {
		open (IN, "</var/lib/csf/csf.tempallow") or die $!;
		@allow = <IN>;
		chomp @allow;
		close (IN);
	}
	foreach my $line (@allow) {
		if ($line eq "") {next}
		my ($time,$ip,$port,$inout,$timeout,$message) = split(/\|/,$line);
		$time = $timeout - (time - $time);
		if ($port eq "") {$port = "*"}
		if ($inout eq "") {$inout = " *"}
		if ($time < 1) {
			$time = "<1";
		} else {
			my $days = int($time/(24*60*60));
			my $hours = ($time/(60*60))%24;
			my $mins = ($time/60)%60;
			my $secs = $time%60;
			$days = $days < 1 ? '' : $days .'d ';
			$hours = $hours < 1 ? '' : $hours .'h ';
			$mins = $mins < 1 ? '' : $mins . 'm ';
			$time = $days . $hours . $mins . $secs . 's'; 
		}
		print "<tr bgcolor='$class'><td>&nbsp;<a href='$script?action=temprm&ip=$ip'><img src='$images/delete.png' border='0' alt='Unblock $ip?'></a>&nbsp;</td><td>ALLOW</td><td>$ip</td><td>$port</td><td>$inout</td><td>$time</td><td>$message</td></tr>\n";
		if ($class eq '#FFFFFF') {$class = '#F4F4EA'} else {$class = '#FFFFFF'}
	}
	print "</table>\n";
	if (@deny or @allow) {
		print "<p align='center'>Flush all temporary IP entries <a href='$script?action=temprm&ip=all'><img src='$images/delete.png' border='0' alt='Unblock All IPs?' valign='middle'></a></p>\n";
		print "<p align='center'>Key: <img src='$images/delete.png' border='0' alt='Unblock'>=Unblock IP, <img valign='middle' src='$images/perm.png' border='0' alt='Permanently Block'>=Permanently Block IP</p>\n";
	} else {
		print "<p align='center'>There are no temporary IP entries</p>\n";
	}
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "temprm") {
	print "<p>Removing temporary entry for $FORM{ip}:</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	if ($FORM{ip} eq "all") {
		&printcmd("/usr/sbin/csf","-tf");
	} else {
		&printcmd("/usr/sbin/csf","-tr",$FORM{ip});
	}
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='action' value='temp'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "temptoperm") {
	print "<p>Permanent ban for $FORM{ip}:</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-tr",$FORM{ip});
	&printcmd("/usr/sbin/csf","-d",$FORM{ip});
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='action' value='temp'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "tempdeny") {
	$FORM{timeout} =~ s/\D//g;
	if ($FORM{dur} eq "minutes") {$FORM{timeout} = $FORM{timeout} * 60}
	if ($FORM{dur} eq "hours") {$FORM{timeout} = $FORM{timeout} * 60 * 60}
	if ($FORM{dur} eq "days") {$FORM{timeout} = $FORM{timeout} * 60 * 60 * 24}
	if ($FORM{ports} eq "") {$FORM{ports} = "*"}
	print "<p>Temporarily $FORM{do}ing $FORM{ip} for $FORM{timeout} seconds:</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	if ($FORM{do} eq "block") {
		&printcmd("/usr/sbin/csf","-td",$FORM{ip},$FORM{timeout},"-p",$FORM{ports},$FORM{comment});
	} else {
		&printcmd("/usr/sbin/csf","-ta",$FORM{ip},$FORM{timeout},"-p",$FORM{ports},$FORM{comment});
	}
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "stop") {
	print "<p>Stopping csf...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-f");
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "disable") {
	print "<p>Disabling csf...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-x");
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "enable") {
	if ($config{DIRECTADMIN} or $config{THIS_UI}) {
		print "<p>Due to restrictions in DirectAdmin you must login to the root shell to enable csf using:\n<p><b>csf -e</b>\n";
	} else {
		print "<p>Enabling csf...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
		&printcmd("/usr/sbin/csf","-e");
		print "</pre>";
	}
	print "</p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "logtail") {
	$FORM{lines} =~ s/\D//g;
	if ($FORM{lines} eq "" or $FORM{lines} == 0) {$FORM{lines} = 30}
	my $script_safe = $script;
	my $CSFfrombot = 120;
	my $CSFfromright = 10;
	if ($config{DIRECTADMIN}) {
		$script = $script_da;
		$CSFfrombot = 400;
		$CSFfromright = 150;
	}
	open (IN, "</etc/csf/csf.syslogs");
	flock (IN, LOCK_SH);
	my @data = <IN>;
	close (IN);
	chomp @data;
	@data = sort @data;
	my $options = "<select id='CSFlognum' onchange='CSFrefreshtimer()'>\n";
	my $cnt = 0;
	foreach my $file (@data) {
		if ($file eq "" or $file =~ /^\#|\s/) {next}
		my @globfiles;
		if ($file =~ /\*|\?|\[/) {
			foreach my $log (glob $file) {push @globfiles, $log}
		} else {push @globfiles, $file}

		foreach my $globfile (@globfiles) {
			if (-f $globfile) {
				my $size = int((stat($globfile))[7]/1024);
				$options .= "<option value='$cnt'";
				if ($globfile eq "/var/log/lfd.log") {$options .= " selected"}
				$options .= ">$globfile ($size kb)</option>\n";
				$cnt++;
			}
		}
	}
	$options .= "</select>\n";
	
	open (IN, "<", "/usr/local/csf/lib/csfajaxtail.js");
	flock (IN, LOCK_SH);
	my @jsdata = <IN>;
	close (IN);
	print "<script>\n";
	print @jsdata;
	print "</script>\n";
	print <<EOF;
<p>$options Lines:<input type='text' id="CSFlines" value="100" size='4'>&nbsp;&nbsp;<button class='input'onclick="CSFrefreshtimer()">Refresh Now</button></p>
<p>Refresh in <span id="CSFtimer">0</span> <button class='input'id="CSFpauseID" onclick="CSFpausetimer()" style="width:80px;">Pause</button> <image src="$images/loader.gif" id="CSFrefreshing" style="display:none" /></p>
<div id="CSFajax" style="overflow:auto;border:solid 1px #990000;width:800px;height:300px"> &nbsp; </div>

<script>
CSFfrombot = $CSFfrombot;
CSFfromright = $CSFfromright;
CSFscript = '$script?action=logtailcmd';
CSFtimer();
</script>
EOF
	if ($config{DIRECTADMIN}) {$script = $script_safe}
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "logtailcmd") {
	$FORM{lines} =~ s/\D//g;
	if ($FORM{lines} eq "" or $FORM{lines} == 0) {$FORM{lines} = 30}

	open (IN, "</etc/csf/csf.syslogs");
	flock (IN, LOCK_SH);
	my @data = <IN>;
	close (IN);
	chomp @data;
	@data = sort @data;
	my $cnt = 0;
	my $logfile = "/var/log/lfd.log";
	my $hit = 0;
	foreach my $file (@data) {
		if ($file eq "" or $file =~ /^\#|\s/) {next}
		my @globfiles;
		if ($file =~ /\*|\?|\[/) {
			foreach my $log (glob $file) {push @globfiles, $log}
		} else {push @globfiles, $file}

		foreach my $globfile (@globfiles) {
			if (-f $globfile) {
				if ($FORM{lognum} == $cnt) {
					$logfile = $globfile;
					$hit = 1;
					last;
				}
				$cnt++;
			}
		}
		if ($hit) {last}
	}

	print "<pre>";
	if (-z $logfile) {
		print "<---- $logfile is currently empty ---->";
	} else {
		if (-x $config{TAIL}) {
			my $timeout = 30;
			eval {
				local $SIG{__DIE__} = undef;
				local $SIG{'ALRM'} = sub {die};
				alarm($timeout);
				my ($childin, $childout);
				my $pid = open3($childin, $childout, $childout,$config{TAIL},"-$FORM{lines}",$logfile);
				while (<$childout>) {
					my $line = $_;
					$line =~ s/&/&amp;/g;
					$line =~ s/</&lt;/g;
					$line =~ s/>/&gt;/g;
					print $line;
				}
				waitpid ($pid, 0);
				alarm(0);
			};
			alarm(0);
			if ($@) {print "TIMEOUT: tail command took too long. Timed out after $timeout seconds\n"}
		} else {
			print "Executable [$config{TAIL}] invalid";
		}
	}
	print "</pre>\n";
}
elsif ($FORM{action} eq "loggrep") {
	$FORM{lines} =~ s/\D//g;
	if ($FORM{lines} eq "" or $FORM{lines} == 0) {$FORM{lines} = 30}
	my $script_safe = $script;
	my $CSFfrombot = 120;
	my $CSFfromright = 10;
	if ($config{DIRECTADMIN}) {
		$script = $script_da;
		$CSFfrombot = 400;
		$CSFfromright = 150;
	}
	open (IN, "</etc/csf/csf.syslogs");
	flock (IN, LOCK_SH);
	my @data = <IN>;
	close (IN);
	chomp @data;
	@data = sort @data;
	my $options = "<select id='CSFlognum' onchange='CSFrefreshtimer()'>\n";
	my $cnt = 0;
	foreach my $file (@data) {
		if ($file eq "" or $file =~ /^\#|\s/) {next}
		my @globfiles;
		if ($file =~ /\*|\?|\[/) {
			foreach my $log (glob $file) {push @globfiles, $log}
		} else {push @globfiles, $file}

		foreach my $globfile (@globfiles) {
			if (-f $globfile) {
				my $size = int((stat($globfile))[7]/1024);
				$options .= "<option value='$cnt'";
				if ($globfile eq "/var/log/lfd.log") {$options .= " selected"}
				$options .= ">$globfile ($size kb)</option>\n";
				$cnt++;
			}
		}
	}
	$options .= "</select>\n";
	
	open (IN, "<", "/usr/local/csf/lib/csfajaxtail.js");
	flock (IN, LOCK_SH);
	my @jsdata = <IN>;
	close (IN);
	print "<script>\n";
	print @jsdata;
	print "</script>\n";
	print <<EOF;
<p>Log: $options</p>
<p style="white-space:nowrap;">Text: <input type='text' size="30" id="CSFgrep" onClick="this.select()">&nbsp;
<input type="checkbox" id="CSFgrep_i" value="1">-i&nbsp;
<input type="checkbox" id="CSFgrep_E" value="1">-E&nbsp;
<input type="checkbox" id="CSFgrep_D" value="1">Detach&nbsp;
<button class='input'onClick="CSFgrep()">Search</button>&nbsp;
<image src="$images/loader.gif" id="CSFrefreshing" style="display:none" /></p>
<div id="CSFajax" style="overflow:auto;border:solid 1px #990000;width:800px;height:300px">
Please Note:
<ul>
	<li>Searches use $config{GREP}, so the search text/regex must be syntactically correct</li>
	<li>Use the "-i" option to ignore case</li>
	<li>Use the "-E" option to perform an extended regular expression search</li>
	<li>Use the "Detach" option to display the search results in a separate window</li>
	<li>Searching large log files can take a long time. This feature has a 30 second timeout</li>
	<li>The searched for text will usually be <span style="background-color:yellow">highlighted</span> but may not always be successful</li>
	<li>This results box will resize to the browser limits when results are displayed</li>
	<li>Only log files listed in /etc/csf/csf.syslogs can be searched. You can add to this file</li>
</ul>
</div>

<script>
CSFfrombot = $CSFfrombot;
CSFfromright = $CSFfromright;
CSFscript = '$script?action=loggrepcmd';
CSFsettimer = 0;
</script>
EOF
	if ($config{DIRECTADMIN}) {$script = $script_safe}
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "loggrepcmd") {
	open (IN, "</etc/csf/csf.syslogs");
	flock (IN, LOCK_SH);
	my @data = <IN>;
	close (IN);
	chomp @data;
	@data = sort @data;
	my $cnt = 0;
	my $logfile = "/var/log/lfd.log";
	my $hit = 0;
	foreach my $file (@data) {
		if ($file eq "" or $file =~ /^\#|\s/) {next}
		my @globfiles;
		if ($file =~ /\*|\?|\[/) {
			foreach my $log (glob $file) {push @globfiles, $log}
		} else {push @globfiles, $file}

		foreach my $globfile (@globfiles) {
			if (-f $globfile) {
				if ($FORM{lognum} == $cnt) {
					$logfile = $globfile;
					$hit = 1;
					last;
				}
				$cnt++;
			}
		}
		if ($hit) {last}
	}
	my @cmd;
	if ($FORM{grepi}) {push @cmd, "-i"}
	if ($FORM{grepE}) {push @cmd, "-E"}
	push @cmd, $FORM{grep};
	push @cmd, $logfile;

	print "<pre>";
	if (-z $logfile) {
		print "<---- $logfile is currently empty ---->";
	} else {
		if (-x $config{GREP}) {
			my $timeout = 30;
			eval {
				local $SIG{__DIE__} = undef;
				local $SIG{'ALRM'} = sub {die};
				alarm($timeout);
				my ($childin, $childout);
				my $pid = open3($childin, $childout, $childout,$config{GREP},@cmd);
				while (<$childout>) {
					my $line = $_;
					$line =~ s/&/&amp;/g;
					$line =~ s/</&lt;/g;
					$line =~ s/>/&gt;/g;
					if ($FORM{grep} ne "") {
						eval {
							local $SIG{__DIE__} = undef;
							if ($FORM{grepi}) {
								$line =~ s/$FORM{grep}/<span style=\"background-color:yellow\">$&<\/span>/ig;
							} else {
								$line =~ s/$FORM{grep}/<span style=\"background-color:yellow\">$&<\/span>/g;
							}
						};
					}
					print $line;
					$total += length $line;
				}
				waitpid ($pid, 0);
				unless ($total) {print "<---- No matches found for \"$FORM{grep}\" in $logfile ---->\n"}
				alarm(0);
			};
			alarm(0);
			if ($@) {print "TIMEOUT: grep command took too long. Timed out after $timeout seconds\n"}
		} else {
			print "Executable [$config{GREP}] invalid";
		}
	}
	print "</pre>\n";
}
elsif ($FORM{action} eq "readme") {
	print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><td><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	open (IN, "</etc/csf/readme.txt") or die $!;
	my @readme = <IN>;
	close (IN);
	chomp @readme;

	foreach my $line (@readme) {
		$line =~ s/\</\&lt\;/g;
		$line =~ s/\>/\&gt\;/g;
		print $line."\n";
	}
	print "</pre></td></tr></table>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "servercheck") {
	print ConfigServer::ServerCheck::report($FORM{verbose});

	open (IN, "</etc/cron.d/csf-cron");
	flock (IN, LOCK_SH);
	my @data = <IN>;
	close (IN);
	chomp @data;
	my $optionselected = "never";
	my $email;
	if (my @ls = grep {$_ =~ /csf \-m/} @data) {
		if ($ls[0] =~ /\@(\w+)\s+root\s+\/usr\/sbin\/csf \-m (.*)/) {$optionselected = $1; $email = $2}
	}
	print "<p align='center'><form action='$script' method='post'><input type='hidden' name='action' value='serverchecksave'>\n";
	print "Generate and email this report <select name='freq'>\n";
	foreach my $option ("never","hourly","daily","weekly","monthly") {
		if ($option eq $optionselected) {print "<option selected>$option</option>\n"} else {print "<option>$option</option>\n"}
	}
	print "</select> to the email address <input type='text' name='email' value='$email'> <input type='submit' class='input' value='Schedule'></form>\n";

	print "<p><form action='$script' method='post'><input type='hidden' name='action' value='servercheck'><input type='hidden' name='verbose' value='1'><input type='submit' class='input' value='Run Again and Display All Checks'></form>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='action' value='servercheck'><input type='submit' class='input' value='Run Again'></form>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form>\n";
}
elsif ($FORM{action} eq "serverchecksave") {
	my $extra = "";
	my $freq = "daily";
	my $email;
	if ($FORM{email} ne "") {$email = "root"}
	if ($FORM{email} =~ /^[a-zA-Z0-9\-\_\.\@\+]+$/) {$email = $FORM{email}}
	foreach my $option ("never","hourly","daily","weekly","monthly") {if ($FORM{freq} eq $option) {$freq = $option}}
	unless ($email) {$freq = "never"; $extra = "(no valid email address supplied)";}
	sysopen (CRON, "/etc/cron.d/csf-cron", O_RDWR | O_CREAT) or die "Unable to open file: $!";
	flock (CRON, LOCK_EX);
	my @data = <CRON>;
	chomp @data;
	seek (CRON, 0, 0);
	truncate (CRON, 0);
	my $done = 0;
	foreach my $line (@data) {
		if ($line =~ /csf \-m/) {
			if ($freq and ($freq ne "never") and !$done) {
				print CRON "\@$freq root /usr/sbin/csf -m $email\n";
				$done = 1;
			}
		} else {
			print CRON "$line\n";
		}
	}
	if (!$done and ($freq ne "never")) {
			print CRON "\@$freq root /usr/sbin/csf -m $email\n";
	}
	close (CRON);

	if ($freq and $freq ne "never") {
		print "<p>Report scheduled to be emailed to $email $freq\n";
	} else {
		print "<p>Report schedule cancelled $extra\n";
	}
	print "<p><form action='$script' method='post'><input type='hidden' name='action' value='servercheck'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "rblcheck") {
	if ($FORM{verbose}) {print "<div id='loading' style='position:absolute; width:100%; text-align:center; top:300px; display: none'>\n	Checking...<br>\n	<img src='$images/csf-loader.gif' border=0><br>\n	This could take some time\n	</div>\n	<script>\n	document.getElementById('loading').style.display = 'block';\n	</script>"}
	my ($status, undef) = ConfigServer::RBLCheck::report($FORM{verbose},$images,1);
	if ($FORM{verbose}) {print "<script>document.getElementById('loading').style.display = 'none'</script>\n"}

	print "<p><b>These options can take a long time to run</b> (several minutes) depending on the number of IP addresses to check and the response speed of the DNS requests:</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='action' value='rblcheck'><input type='hidden' name='verbose' value='1'><input type='submit' class='input' value='Update All Checks (standard)'> Generates the normal report showing exceptions only</form></p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='action' value='rblcheck'><input type='hidden' name='verbose' value='2'><input type='submit' class='input' value='Update All Checks (verbose)'> Generates the normal report but shows successes and failures</form></p>\n";
	print "<br><p><form action='$script' method='post'><input type='hidden' name='action' value='rblcheckedit'><input type='submit' class='input' value='Edit RBL Options'> Edit csf.rblconf to enable and disable IPs and RBLs</form></p>\n";

	open (IN, "</etc/cron.d/csf-cron");
	flock (IN, LOCK_SH);
	my @data = <IN>;
	close (IN);
	chomp @data;
	my $optionselected = "never";
	my $email;
	if (my @ls = grep {$_ =~ /csf \-\-rbl/} @data) {
		if ($ls[0] =~ /\@(\w+)\s+root\s+\/usr\/sbin\/csf \-\-rbl (.*)/) {$optionselected = $1; $email = $2}
	}
	print "<p align='center'><form action='$script' method='post'><input type='hidden' name='action' value='rblchecksave'>\n";
	print "Generate and email this report <select name='freq'>\n";
	foreach my $option ("never","hourly","daily","weekly","monthly") {
		if ($option eq $optionselected) {print "<option selected>$option</option>\n"} else {print "<option>$option</option>\n"}
	}
	print "</select> to the email address <input type='text' name='email' value='$email'> <input type='submit' class='input' value='Schedule'></form>\n";

	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form>\n";
}
elsif ($FORM{action} eq "rblchecksave") {
	my $extra = "";
	my $freq = "daily";
	my $email;
	if ($FORM{email} ne "") {$email = "root"}
	if ($FORM{email} =~ /^[a-zA-Z0-9\-\_\.\@\+]+$/) {$email = $FORM{email}}
	foreach my $option ("never","hourly","daily","weekly","monthly") {if ($FORM{freq} eq $option) {$freq = $option}}
	unless ($email) {$freq = "never"; $extra = "(no valid email address supplied)";}
	sysopen (CRON, "/etc/cron.d/csf-cron", O_RDWR | O_CREAT) or die "Unable to open file: $!";
	flock (CRON, LOCK_EX);
	my @data = <CRON>;
	chomp @data;
	seek (CRON, 0, 0);
	truncate (CRON, 0);
	my $done = 0;
	foreach my $line (@data) {
		if ($line =~ /csf \-\-rbl/) {
			if ($freq and ($freq ne "never") and !$done) {
				print CRON "\@$freq root /usr/sbin/csf --rbl $email\n";
				$done = 1;
			}
		} else {
			print CRON "$line\n";
		}
	}
	if (!$done and ($freq ne "never")) {
			print CRON "\@$freq root /usr/sbin/csf --rbl $email\n";
	}
	close (CRON);

	if ($freq and $freq ne "never") {
		print "<p>Report scheduled to be emailed to $email $freq\n";
	} else {
		print "<p>Report schedule cancelled $extra\n";
	}
	print "<p><form action='$script' method='post'><input type='hidden' name='action' value='rblcheck'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "rblcheckedit") {
	&editfile("/etc/csf/csf.rblconf","saverblcheckedit");
	print "<p><form action='$script' method='post'><input type='hidden' name='action' value='rblcheck'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "saverblcheckedit") {
	&savefile("/etc/csf/csf.rblconf","");
	print "<p><form action='$script' method='post'><input type='hidden' name='action' value='rblcheck'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "restartboth") {
	print "<p>Restarting csf...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-sf");
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	if ($config{DIRECTADMIN} or $config{THIS_UI}) {
		print "<p>Signal lfd to <i>restart</i>...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
		sysopen (OUT, "/var/lib/csf/lfd.restart",, O_WRONLY | O_CREAT) or die "Unable to open file: $!";
		close (OUT);
	} else {
		print "<p>Restarting lfd...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
		ConfigServer::Service::restartlfd();
	}
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "remapf") {
	print "<p>Removing APF/BFD...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("sh","/usr/local/csf/bin/remove_apf_bfd.sh");
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><b>Note: You should check the root cron and /etc/crontab to ensure that there are no apf or bfd related cron jobs remaining</b></p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "qallow") {
	print "<p>Allowing $FORM{ip}...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-a",$FORM{ip},$FORM{comment});
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "qdeny") {
	print "<p>Blocking $FORM{ip}...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-d",$FORM{ip},$FORM{comment});
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "qignore") {
	print "<p>Ignoring $FORM{ip}...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	open (OUT, ">>", "/etc/csf/csf.ignore");
	print OUT "$FORM{ip}\n";
	close (OUT);
	print "</p>\n<p>...<b>Done</b>.</p>\n";
	if ($config{DIRECTADMIN} or $config{THIS_UI}) {
		print "<p>Signal lfd to <i>restart</i>...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
		sysopen (OUT, "/var/lib/csf/lfd.restart",, O_WRONLY | O_CREAT) or die "Unable to open file: $!";
		close (OUT);
	} else {
		print "<p>Restarting lfd...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
		ConfigServer::Service::restartlfd();
	}
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "kill") {
	print "<p>Unblock $FORM{ip}, trying permanent blocks...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-dr",$FORM{ip});
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p>Unblock $FORM{ip}, trying temporary blocks...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-tr",$FORM{ip});
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "grep") {
	print "<p>Searching for $FORM{ip}...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	my ($childin, $childout);
	my $pid = open3($childin, $childout, $childout, "/usr/sbin/csf","-g",$FORM{ip});
	my $unblock;
	while (<$childout>) {
		my $line = $_;
		if ($line =~ /^csf.deny:\s(\S+)\s*/) {$unblock = 1}
		if ($line =~ /^Temporary Blocks: IP:(\S+)\s*/) {$unblock = 1}
		print $_;
	}
	waitpid ($pid, 0);
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	if ($unblock) {print "<p>Unblock $FORM{ip}: <a href='$script?action=kill&ip=$FORM{ip}'><img src='$images/delete.png' border='0' alt='Unblock $FORM{ip}?'></a></p>\n"}
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "callow") {
	print "<p>Cluster Allow $FORM{ip}...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-ca",$FORM{ip});
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "cdeny") {
	print "<p>Cluster Deny $FORM{ip}...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-cd",$FORM{ip});
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "crm") {
	print "<p>Cluster Remove $FORM{ip}...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-cr",$FORM{ip});
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "cping") {
	print "<p>Cluster PING...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-cp");
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "cconfig") {
	$FORM{option} =~ s/\s*//g;
	my %restricted;
	if ($config{RESTRICT_UI}) {
		sysopen (IN, "/usr/local/csf/lib/restricted.txt", O_RDWR | O_CREAT) or die "Unable to open file: $!";
		flock (IN, LOCK_SH);
		while (my $entry = <IN>) {
			chomp $entry;
			$restricted{$entry} = 1;
		}
		close (IN);
	}
	if ($restricted{$FORM{option}}) {
		print "Option $FORM{option} cannot be set with RESTRICT_UI enabled\n";
		exit;
	}
	print "<p>Cluster configuration option...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-cc",$FORM{option},$FORM{value});
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "crestart") {
	print "<p>Cluster restart csf and lfd...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf --crestart");
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "allow") {
	&editfile("/etc/csf/csf.allow","saveallow");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "saveallow") {
	&savefile("/etc/csf/csf.allow","both");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "redirect") {
	&editfile("/etc/csf/csf.redirect","saveredirect");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "saveredirect") {
	&savefile("/etc/csf/csf.redirect","both");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "smtpauth") {
	&editfile("/etc/csf/csf.smtpauth","savesmtpauth");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "savesmtpauth") {
	&savefile("/etc/csf/csf.smtpauth","both");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "reseller") {
	&editfile("/etc/csf/csf.resellers","savereseller");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "savereseller") {
	&savefile("/etc/csf/csf.resellers","");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "dirwatch") {
	&editfile("/etc/csf/csf.dirwatch","savedirwatch");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "savedirwatch") {
	&savefile("/etc/csf/csf.dirwatch","lfd");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "dyndns") {
	&editfile("/etc/csf/csf.dyndns","savedyndns");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "savedyndns") {
	&savefile("/etc/csf/csf.dyndns","lfd");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "blocklists") {
	&editfile("/etc/csf/csf.blocklists","saveblocklists");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "saveblocklists") {
	&savefile("/etc/csf/csf.blocklists","both");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "syslogusers") {
	&editfile("/etc/csf/csf.syslogusers","savesyslogusers");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "savesyslogusers") {
	&savefile("/etc/csf/csf.syslogusers","lfd");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "logfiles") {
	&editfile("/etc/csf/csf.logfiles","savelogfiles");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "savelogfiles") {
	&savefile("/etc/csf/csf.logfiles","lfd");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "deny") {
	&editfile("/etc/csf/csf.deny","savedeny");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "savedeny") {
	&savefile("/etc/csf/csf.deny","both");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "templates") {
	&editfile("/usr/local/csf/tpl/$FORM{template}","savetemplates","template");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "savetemplates") {
	&savefile("/usr/local/csf/tpl/$FORM{template}","",1);
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "ignorefiles") {
	&editfile("/etc/csf/$FORM{ignorefile}","saveignorefiles","ignorefile");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "saveignorefiles") {
	&savefile("/etc/csf/$FORM{ignorefile}","lfd");
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "conf") {
	sysopen (IN, "/etc/csf/csf.conf", O_RDWR | O_CREAT) or die "Unable to open file: $!";
	flock (IN, LOCK_SH);
	my @confdata = <IN>;
	close (IN);
	chomp @confdata;

	my %restricted;
	if ($config{RESTRICT_UI}) {
		sysopen (IN, "/usr/local/csf/lib/restricted.txt", O_RDWR | O_CREAT) or die "Unable to open file: $!";
		flock (IN, LOCK_SH);
		while (my $entry = <IN>) {
			chomp $entry;
			$restricted{$entry} = 1;
		}
		close (IN);
	}

	print <<EOF;
<script type="text/javascript">
function CSFexpand(obj){
	if (!obj.savesize) {obj.savesize=obj.size;}
	var newsize = Math.max(obj.savesize,obj.value.length);
	if (newsize > 120) {newsize = 120;}
	obj.size = newsize;
}
</script>
<style>
input[type=text], textarea, select {
	font-family: Courier New, Courier;
	font-size: 14px;
}
</style>
EOF
	print "<fieldset><legend><b>Edit ConfigServer Firewall</b></legend>\n";
	open (IN, "<", "/usr/local/csf/lib/csf.div");
	my @divdata = <IN>;
	close (IN);
	print @divdata;
	print "<div id='paginatediv2' class='paginationstyle' align='center'></div>\n";
	print "<form action='$script' method='post'>\n";
	print "<input type='hidden' name='action' value='saveconf'>\n";
	print "<table align='center' style='background: white; color:black; font-family: Courier New, Courier; font-size: 12px' width='95%'>\n<tr><td>\n";
	my $first = 1;
	my @divnames;
	my $comment = 0;
	foreach my $line (@confdata) {
		if (($line !~ /^\#/) and ($line =~ /=/)) {
			if ($comment) {print "</div>\n"}
			$comment = 0;
			my ($start,$end) = split (/=/,$line,2);
			my $name = $start;
			my $cleanname = $start;
			$cleanname =~ s/\s//g;
			$name =~ s/\s/\_/g;
			if ($end =~ /\"(.*)\"/) {$end = $1}
			my $size = length($end) + 4;
			my $class = "value-default";
			my ($status,$range,$default) = sanity($start,$end);
			my $showrange = "";
			if ($default ne "") {
				$showrange = " Default: $default [$range]";
				if ($end ne $default) {$class = "value-other"}
			}
			if ($status) {$class = "value-warning"; $showrange = " Recommended range: $range (Default: $default)"}
			if ($config{RESTRICT_UI} and ($cleanname eq "CLUSTER_KEY" or $cleanname eq "UI_PASS" or $cleanname eq "UI_USER")) {
				print "<div class='$class'><b>$start</b> = <input type='text' value='********' size='14' disabled> (hidden restricted UI item)</div>\n";
			}
			elsif ($restricted{$cleanname}) {
				print "<div class='$class'><b>$start</b> = <input type='text' onFocus='CSFexpand(this);' onkeyup='CSFexpand(this);' value='$end' size='$size' disabled> (restricted UI item)</div>\n";
			} else {
				print "<div class='$class'><b>$start</b> = <input type='text' onFocus='CSFexpand(this);' onkeyup='CSFexpand(this);' name='$name' value='$end' size='$size'>$showrange</div>\n";
			}
		} else {
			if ($line =~ /^\# SECTION:(.*)/) {
				push @divnames, $1;
				unless ($first) {print "</div>\n"}
				print "<div class='virtualpage hidepiece'>\n<div class='section'>";
				print "$1</div>\n";
				$first = 0;
				next;
			}
			if ($line =~ /^\# / and $comment == 0) {
				$comment = 1;
				print "<div class='comment'>\n";
			}
			$line =~ s/\#//g;
			$line =~ s/&/&amp;/g;
			$line =~ s/</&lt;/g;
			$line =~ s/>/&gt;/g;
			$line =~ s/\n/<br \/>\n/g;
			print "$line<br />\n";
		}
	}
	print "</div></td></tr></table>\n";
	print "<div id='paginatediv' class='paginationstyle' align='center'>\n<a href='javascript:pagecontent.showall()'>Show All</a> <a href='#' rel='previous'>Prev</a> <select style='width: 250px'></select> <a href='#' rel='next'>Next</a>\n</div>\n";
	print "</fieldset>\n";
	print <<EOD;
<script type="text/javascript">

var pagecontent=new virtualpaginate({
 piececlass: "virtualpage", //class of container for each piece of content
 piececontainer: "div", //container element type (ie: "div", "p" etc)
 pieces_per_page: 1, //Pieces of content to show per page (1=1 piece, 2=2 pieces etc)
 defaultpage: 0, //Default page selected (0=1st page, 1=2nd page etc). Persistence if enabled overrides this setting.
 wraparound: false,
 persist: false //Remember last viewed page and recall it when user returns within a browser session?
})
EOD
	print "pagecontent.buildpagination(['paginatediv','paginatediv2'],[";
	foreach my $line (@divnames) {print "'$line',"}
	print "''])\npagecontent.showall();\n</script>\n";
	print "<p align='center'><input type='submit' class='input' value='Change'></p>\n";
	print "</form>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "saveconf") {
	sysopen (IN, "/etc/csf/csf.conf", O_RDWR | O_CREAT) or die "Unable to open file: $!";
	flock (IN, LOCK_SH);
	my @confdata = <IN>;
	close (IN);
	chomp @confdata;

	my %restricted;
	if ($config{RESTRICT_UI}) {
		sysopen (IN, "/usr/local/csf/lib/restricted.txt", O_RDWR | O_CREAT) or die "Unable to open file: $!";
		flock (IN, LOCK_SH);
		while (my $entry = <IN>) {
			chomp $entry;
			$restricted{$entry} = 1;
		}
		close (IN);
	}

	sysopen (OUT, "/etc/csf/csf.conf", O_WRONLY | O_CREAT) or die "Unable to open file: $!";
	flock (OUT, LOCK_EX);
	seek (OUT, 0, 0);
	truncate (OUT, 0);
	for (my $x = 0; $x < @confdata;$x++) {
		if (($confdata[$x] !~ /^\#/) and ($confdata[$x] =~ /=/)) {
			my ($start,$end) = split (/=/,$confdata[$x],2);
			if ($end =~ /\"(.*)\"/) {$end = $1}
			my $name = $start;
			my $sanity_name = $start;
			$name =~ s/\s/\_/g;
			$sanity_name =~ s/\s//g;
			if ($restricted{$sanity_name}) {
				print OUT "$confdata[$x]\n";
			} else {
				print OUT "$start= \"$FORM{$name}\"\n";
				$end = $FORM{$name};
			}
		} else {
			print OUT "$confdata[$x]\n";
		}
	}
	close (OUT);
	ConfigServer::Config::resetconfig();
	my $newconfig = ConfigServer::Config->loadconfig();
	my %newconfig = $config->config;
	foreach my $key (keys %newconfig) {
		my ($insane,$range,$default) = sanity($key,$newconfig{$key});
		if ($insane) {print "<br>WARNING: $key sanity check. $key = \"$newconfig{$key}\". Recommended range: $range (Default: $default)\n"}
	}

	print "<p>Changes saved. You should restart both csf and lfd.</p>\n";
	print "<p align='center'><form action='$script' method='post'><input type='hidden' name='action' value='restartboth'><input type='submit' class='input' value='Restart csf+lfd'></form></p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "viewlogs") {
	if (-e "/var/lib/csf/stats/iptables_log") {
		open (IN, "<", "/var/lib/csf/stats/iptables_log") or die "Unable to open file: $!";
		flock (IN, LOCK_SH);
		my @iptables = <IN>;
		close (IN);
		chomp @iptables;
		@iptables = reverse @iptables;
		my $from;
		my $to;
		my $divcnt = 0;
		my $expcnt = @iptables;
		my $class = '#F4F4EA';

		if ($iptables[0] =~ /\|(\S+\s+\d+\s+\S+)/) {$from = $1}
		if ($iptables[-1] =~ /\|(\S+\s+\d+\s+\S+)/) {$to = $1}

		print "<p align='center'><big>Last $config{ST_IPTABLES} iptables logs*, latest:<b>$from</b> oldest:<b>$to</b></big></p>\n";

		print <<EOF;
<script language="JavaScript">

function showMenu(divNum) {
	var id = "s" + divNum;
	if (document.getElementById(id).style.display != "table-row") {
		document.getElementById(id).style.display = "table-row";
		document.images["i" + divNum].src = "$images/minus.png";
	} else {
		document.getElementById(id).style.display = "none";
		document.images["i" + divNum].src = "$images/plus.png";
	}
}

function expandO( ec ,totNum ) {
	for (j=1; j<totNum + 1; j++) {
		var id = "s" + j;
		if (ec == "expand") {
			document.getElementById(id).style.display = "table-row";
			document.images["i" + j].src = "$images/minus.png";
		} else {
			document.getElementById(id).style.display = "none";
			document.images["i" + j].src = "$images/plus.png";
		}
	}
}
</script>
<style>
td {padding: 5px;}
</style>
EOF
		print "<br><table align='center' cellpadding='4' cellspacing='1' width='95%' align='center' bgcolor='#990000'>\n";
		print "<tr bgcolor='#F4F4EA'><td colspan='7'>";
		print " <a href='javascript:expandO(\"expand\",$expcnt);'><img valign='absmiddle' src='$images/plus.png' name='i$divcnt' border='0'></a>\n";
		print " <a href='javascript:expandO(\"expand\",$expcnt);'>Expand All</a>\n";
		print "&nbsp;&nbsp;<a href='javascript:expandO(\"collapse\",$expcnt);'><img valign='absmiddle' src='$images/minus.png' name='i$divcnt' border='0'></a>\n";
		print " <a href='javascript:expandO(\"collapse\",$expcnt);'>Collapse All</a>\n";
		print "</td></tr>\n";
		print "<tr bgcolor='#FFFFFF'><td><b>Time</b></td><td width='50%'><b>From</b></td><td><b>Port</b></td><td><b>I/O</b></td><td width='50%'><b>To</b></td><td><b>Port</b></td><td><b>Proto</b></td></tr>\n";
		my $size = scalar @iptables;
		if ($size > $config{ST_IPTABLES}) {$size = $config{ST_IPTABLES}}
		for (my $x = 0 ;$x < $size ;$x++) {
			my $line = $iptables[$x];
			$divcnt++;
			my ($text,$log) = split(/\|/,$line);
			my ($time,$desc,$in,$out,$src,$dst,$spt,$dpt,$proto,$inout);
			if ($log =~ /IN=(\S+)/) {$in = $1}
			if ($log =~ /OUT=(\S+)/) {$out = $1}
			if ($log =~ /SRC=(\S+)/) {$src = $1}
			if ($log =~ /DST=(\S+)/) {$dst = $1}
			if ($log =~ /SPT=(\d+)/) {$spt = $1}
			if ($log =~ /DPT=(\d+)/) {$dpt = $1}
			if ($log =~ /PROTO=(\S+)/) {$proto = $1}

			if ($text ne "") {
				$text =~ s/\(/\<br\>\(/g;
				if ($in and $src) {$src = $text ; $dst .= " <br>(server)"}
				elsif ($out and $dst) {$dst = $text ; $src .= " <br>(server)"}
			}
			if ($log =~ /^(\S+\s+\d+\s+\S+)/) {$time = $1}

			$inout = "n/a";
			if ($in) {$inout = "in"}
			elsif ($out) {$inout = "out"}

			print "<tr bgcolor='$class'><td nowrap><a href='javascript:showMenu($divcnt);'><img valign='absmiddle' src='$images/plus.png' name='i$divcnt' border='0'></a> $time</td><td>$src</td><td>$spt</td><td>$inout</td><td>$dst</td><td>$dpt</td><td>$proto</td></tr>\n";

			$log =~ s/\&/\&amp\;/g;
			$log =~ s/>/\&gt\;/g;
			$log =~ s/</\&lt\;/g;
			print "<tr bgcolor='$class' style='display:none' id='s$divcnt'><td colspan='7'><span>$log</span></td></tr>\n";
			if ($class eq '#FFFFFF') {$class = '#F4F4EA'} else {$class = '#FFFFFF'}
		}
		print "</table>\n";
		print "<p>* These iptables logs taken from $config{IPTABLES_LOG} will not necessarily show all packets blocked by iptables. For example, ports listed in DROP_NOLOG or the settings for DROP_LOGGING/DROP_IP_LOGGING/DROP_ONLYRES/DROP_PF_LOGGING will affect what is logged. Additionally, there is rate limiting on all iptables log rules to prevent log file flooding</p>\n";
	} else {
		print "<p> No logs entries found<p>\n";
	}

	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "sips") {
	sysopen (IN, "/etc/csf/csf.sips", O_RDWR | O_CREAT) or die "Unable to open file: $!";
	flock (IN, LOCK_SH);
	my @confdata = <IN>;
	close (IN);
	chomp @confdata;

	print "<form action='$script' method='post'><input type='hidden' name='action' value='sipsave'><br>\n";
	print "<table align='center' border='0' cellspacing='0' cellpadding='4' bgcolor='FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr bgcolor='#FFFFFF'><td><b>IP Address</b></td><td><b>Deny All Access to IP</b></td></tr>\n";
	my $class = '#F4F4EA';

	my %sips;
	open(IN,"<","/etc/csf/csf.sips");
	my @data = <IN>;
	close(IN);
	chomp @data;
	foreach my $line (@data) {
		if ($line =~ /^\d+\.\d+\.\d+\.\d+$/) {$sips{$line} = 1}
	}

	my ($childin, $childout);
	my $pid = open3($childin, $childout, $childout, $config{IFCONFIG});
	my @ifconfig = <$childout>;
	waitpid ($pid, 0);
	chomp @ifconfig;

	foreach my $line (@ifconfig) {
		if ($line =~ /inet.*?($ipv4reg)/) {
			my $ip = $1;
			if ($ip =~ /^127\.0\.0/) {next}
			my $chk = "ip_$ip";
			$chk =~ s/\./\_/g;
			my $checked = "";
			if ($sips{$ip}) {$checked = "checked"}
			print "<tr bgcolor='$class'><td>$ip</td><td align='center'><input type='checkbox' name='$chk' $checked></td></tr>\n";
			if ($class eq '#FFFFFF') {$class = '#F4F4EA'} else {$class = '#FFFFFF'}
		}
	}

	print "<tr bgcolor='$class'><td colspan='3' align='center'><input type='submit' class='input' value='Change'></td></tr>\n";
	print "</table></form>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "sipsave") {
	open(IN,"<","/etc/csf/csf.sips");
	my @data = <IN>;
	close(IN);
	chomp @data;

	open(OUT,">","/etc/csf/csf.sips");
	foreach my $line (@data) {
		if ($line =~ /^\#/) {print OUT "$line\n"} else {last}
	}
	foreach my $key (keys %FORM) {
		if ($key =~ /^ip_(.*)/) {
			my $ip = $1;
			$ip =~ s/\_/\./g;
			print OUT "$ip\n";
		}
	}
	close(OUT);

	print "<p>Changes saved. You should restart csf.</p>\n";
	print "<p align='center'><form action='$script' method='post'><input type='hidden' name='action' value='restart'><input type='submit' class='input' value='Restart csf'></form></p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "upgrade") {
	if ($config{DIRECTADMIN}) {
		print "<p>Due to restrictions in DirectAdmin you must login to the root shell to upgrade csf using:\n<p><b>csf -u</b>\n";
	}
	elsif ($config{THIS_UI}) {
		print "<p>You cannot upgrade through the UI as restarting lfd will interrupt this session. You must login to the root shell to upgrade csf using:\n<p><b>csf -u</b>\n";
	} else {
		print "<p>Upgrading csf...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
		&printcmd("/usr/sbin/csf","-u");
		print "</pre></p>\n<p>...<b>Done</b>.</p>\n";

		open (IN, "</etc/csf/version.txt") or die $!;
		$myv = <IN>;
		close (IN);
		chomp $myv;
	}

	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "denyf") {
	print "<p>Removing all entries from csf.deny...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","-df");
	&printcmd("/usr/sbin/csf","-tf");
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";

	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "csftest") {
	print "<p>Testing iptables...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/local/csf/bin/csftest.pl");
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p>You should restart csf after having run this test.</p>\n";
	print "<p align='center'><form action='$script' method='post'><input type='hidden' name='action' value='restart'><input type='submit' class='input' value='Restart csf'></form></p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "profiles") {
	my @profiles = sort glob("/usr/local/csf/profiles/*");
	my @backups = reverse glob("/var/lib/csf/backup/*");
	my $color = "#F4F4EA";

	print "<form action='$script' method='post'><input type='hidden' name='action' value='profileapply'>\n";
	print "<table align='center' border='0' width='95%' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><th>Preconfigured Profiles</th><th align='center' style='border-left:1px solid #990000'>&nbsp;</th></tr>\n";
	foreach my $profile (@profiles) {
		my ($file, undef) = fileparse($profile);
		$file =~ s/\.conf$//;
		my $text;
		open (IN, "<", $profile);
		flock (IN, LOCK_SH);
		my @profiledata = <IN>;
		close (IN);
		chomp @profiledata;

		if ($file eq "reset_to_defaults") {
			$text = "This is the installation default profile and will reset all csf.conf settings, including enabling TESTING mode";
		}
		elsif ($profiledata[0] =~ /^\# Profile:/) {
			foreach my $line (@profiledata) {
				if ($line =~ /^\# (.*)$/) {$text .= "$1 "}
			}
		}

		print "<tr bgcolor='$color'><td><b>$file</b><br>\n$text</td><td align='center' style='border-left:1px solid #990000'><input type='radio' name='profile' value='$file'></td></tr>\n";
		if ($color eq "#F4F4EA") {$color = "#FFFFFF"} else {$color = "#F4F4EA"}
	}
	print "<tr bgcolor='$color'><td>You can apply one or more of these profiles to csf.conf. Apart from reset_to_defaults, most of these profiles contain only a subset of settings. You can find out what will be changed by comparing the profile to the current configuration below. A backup of csf.conf will be created before any profile is applied.</td><td align='center' style='border-left:1px solid #990000'><input type='submit' class='input' value='Apply Profile'></td></tr>\n";
	print "</table>\n";
	print "</form>\n";

	print "<br><form action='$script' method='post'><input type='hidden' name='action' value='profilebackup'>\n";
	print "<table align='center' border='0' width='95%' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><th>Backup csf.conf</th></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td>Create a backup of csf.conf. You can use an optional name for the backup that should only contain alphanumerics. Other characters (including spaces) will be replaced with an underscore ( _ )</td></tr>\n";
	print "<tr><td align='center'><input type='text' size='40' name='backup' placeholder='Optional name'> <input type='submit' class='input' value='Create Backup'></td></tr>\n";
	print "</table>\n";
	print "</form>\n";

	print "<br><form action='$script' method='post'><input type='hidden' name='action' value='profilerestore'>\n";
	print "<table align='center' border='0' width='95%' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><th>Restore Backup Of csf.conf</th></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td align='center'><select name='backup' size='10' style='min-width:400px'>\n";
	foreach my $backup (@backups) {
		my ($file, undef) = fileparse($backup);
		my ($stamp,undef) = split(/_/,$file);
		print "<optgroup label='".localtime($stamp).":'><option>$file</option></optgroup>\n";
	}
	print "</select></td></tr>\n";
	print "<tr><td align='center'><input type='submit' class='input' value='Restore Backup'></td></tr>\n";
	print "</table>\n";
	print "</form>\n";

	print "<br><form action='$script' method='post'><input type='hidden' name='action' value='profilediff'>\n";
	print "<table align='center' border='0' width='95%' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><th>Compare Configurations</th></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td align='center'>Select first configuration:<br>\n<select name='profile1' size='10' style='min-width:400px'>\n";
	print "<optgroup label='Profiles:'>\n";
	foreach my $profile (@profiles) {
		my ($file, undef) = fileparse($profile);
		$file =~ s/\.conf$//;
		print "<option>$file</option>\n";
	}
	print "</optgroup>\n";
	foreach my $backup (@backups) {
		my ($file, undef) = fileparse($backup);
		my ($stamp,undef) = split(/_/,$file);
		print "<optgroup label='".localtime($stamp).":'><option>$file</option></optgroup>\n";
	}
	print "</select></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td align='center' style='border-top:1px dashed #990000'>Select second configuration:<br>\n<select name='profile2' size='10' style='min-width:400px'>\n";
	print "<optgroup label='Current Configuration:'><option value='current' selected>/etc/csf/csf.conf</option></optgroup>\n";
	print "<optgroup label='Profiles:'>\n";
	foreach my $profile (@profiles) {
		my ($file, undef) = fileparse($profile);
		$file =~ s/\.conf$//;
		print "<option>$file</option>\n";
	}
	print "</optgroup>\n";
	foreach my $backup (@backups) {
		my ($file, undef) = fileparse($backup);
		my ($stamp,undef) = split(/_/,$file);
		print "<optgroup label='".localtime($stamp).":'><option>$file</option></optgroup>\n";
	}
	print "</select></td></tr>\n";
	print "</select></td></tr>\n";
	print "<tr><td align='center'><input type='submit' class='input' value='Compare Config/Backup/Profile Settings'></td></tr>\n";
	print "</table>\n";
	print "</form>\n";

	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "profileapply") {
	my $profile = $FORM{profile};
	$profile =~ s/\W/_/g;
	print "<p>Applying profile ($profile)...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","--profile","apply",$profile);
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p>You should restart both csf and lfd.</p>\n";
	print "<p align='center'><form action='$script' method='post'><input type='hidden' name='action' value='restartboth'><input type='submit' class='input' value='Restart csf+lfd'></form></p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "profilebackup") {
	my $profile = $FORM{backup};
	$profile =~ s/\W/_/g;
	print "<p>Creating backup...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","--profile","backup",$profile);
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "profilerestore") {
	my $profile = $FORM{backup};
	$profile =~ s/\W/_/g;
	print "<p>Restoring backup ($profile)...</p>\n<p><pre style='font-family: Courier New, Courier; font-size: 12px'>\n";
	&printcmd("/usr/sbin/csf","--profile","restore",$profile);
	print "</pre></p>\n<p>...<b>Done</b>.</p>\n";
	print "<p>You should restart both csf and lfd.</p>\n";
	print "<p align='center'><form action='$script' method='post'><input type='hidden' name='action' value='restartboth'><input type='submit' class='input' value='Restart csf+lfd'></form></p>\n";
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "profilediff") {
	my $profile1 = $FORM{profile1};
	my $profile2 = $FORM{profile2};
	$profile2 =~ s/\W/_/g;
	$profile2 =~ s/\W/_/g;
	$color = "#FFFFFF";

	print "<table align='center' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	my ($childin, $childout);
	my $pid = open3($childin, $childout, $childout, "/usr/sbin/csf","--profile","diff",$profile1,$profile2);
	while (<$childout>) {
		$_ =~ s/\[|\]//g;
		my ($var,$p1,$p2) = split(/\s+/,$_);
		if ($var eq "") {
			next;
		}
		elsif ($var eq "SETTING") {
			print "<tr bgcolor='$color'><td><b>$var</b></td><td align='center'><b>$p1</b></td><td align='center'><b>$p2</b></td></tr>\n";
		}
		else {
			print "<tr bgcolor='$color'><td>$var</td><td align='center'>$p1</td><td align='center'>$p2</td></tr>\n";
		}
		if ($color eq "#FFFFFF") {$color = "#F4F4EA"} else {$color = "#FFFFFF"}
	}
	waitpid ($pid, 0);
	print "</table>\n";

	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($FORM{action} eq "viewports") {
	$class = "#F4F4EA";
	print "<style>\ntd {padding: 5px;}\n</style>\n";

	print "<h2>Ports listening for external connections and the executables running behind them:</h2>\n";
	print "<table align='center' cellpadding='4' cellspacing='1' width='95%' align='center' bgcolor='#990000'>\n";
	print "<tr bgcolor='#FFFFFF'><td align='left'><b>Port</td><td align='left'><b>Protocol</b></td><td align='left'><b>Open</td><td align='left'><b>Conns</td><td align='left'><b>PID</td><td align='left'><b>User</b></td><td align='left'><b>Command Line</b></td><td align='left'><b>Executable</b></td></tr>\n";
	my %listen = ConfigServer::Ports->listening;
	my %ports = ConfigServer::Ports->openports;
	foreach my $protocol (sort keys %listen) {
		foreach my $port (sort {$a <=> $b} keys %{$listen{$protocol}}) {
			foreach my $pid (sort {$a <=> $b} keys %{$listen{$protocol}{$port}}) {
				my $fopen;
				if ($ports{$protocol}{$port}) {$fopen = "4"} else {$fopen = "-"}
				if ($config{IPV6} and $ports{$protocol."6"}{$port}) {$fopen .= "/6"} else {$fopen .= "/-"}

				my $fcmd = ($listen{$protocol}{$port}{$pid}{cmd});
				$fcmd =~ s/\</\&lt;/g;
				$fcmd =~ s/\&/\&amp;/g;
				if (length $fcmd > 40) {$fcmd = substr($fcmd,0,40)."..."}

				my $fexe = $listen{$protocol}{$port}{$pid}{exe};
				my $fconn = $listen{$protocol}{$port}{$pid}{conn};
				print "<tr bgcolor='$class'><td>$port</td><td>$protocol</td><td>$fopen</td><td>$fconn</td><td>$pid</td><td>$listen{$protocol}{$port}{$pid}{user}</td><td>$fcmd</td><td>$fexe</td></tr>\n";
				if ($class eq '#FFFFFF') {$class = '#F4F4EA'} else {$class = '#FFFFFF'}
			}
		}
	}
	print "</table>\n";

	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
elsif ($mobile) {
	print "<table align='center' border='0' width='95%' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='hidden' name='action' value='qallow'><input type='submit' class='input' value='Quick Allow'></td><td width='100%'><input type='text' name='ip' value='' size='18' style='background-color: lightgreen'></form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='hidden' name='action' value='qdeny'><input type='submit' class='input' value='Quick Deny'></td><td width='100%'><input type='text' name='ip' value='' size='18' style='background-color: pink'></form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='hidden' name='action' value='qignore'><input type='submit' class='input' value='Quick Ignore'></td><td width='100%'><input type='text' name='ip' value='' size='18' style='background-color: lightblue'></form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='mobi' value='$mobile'><input type='hidden' name='action' value='kill'><input type='submit' class='input' value='Quick Unblock'></td><td width='100%'><input type='text' name='ip' value='' size='18'></form></td></tr>\n";
	print "</table>\n";
}
else {
	if (defined $ENV{WEBMIN_VAR} and defined $ENV{WEBMIN_CONFIG}) {
		unless (-l "index.cgi") {
			unlink "index.cgi";
			my $status = symlink ("/usr/local/csf/lib/webmin/csf/index.cgi","index.cgi");
			if ($status and -l "index.cgi") {
				symlink ("/usr/local/csf/lib/webmin/csf/images","csfimages");
				print "<p><b>csf updated to symlink webmin module to /usr/local/csf/lib/webmin/csf/. Click <a href='index.cgi'>here</a> to continue<p></b>\n";
				exit;
			} else {
				print "<p>Failed to symlink to /usr/local/csf/lib/webmin/csf/<p>\n";
			}
		}
	}

	&getethdev;
	my ($childin, $childout);
	my $pid = open3($childin, $childout, $childout, $config{IPTABLES},"-L","LOCALINPUT","-n");
	my @iptstatus = <$childout>;
	waitpid ($pid, 0);
	chomp @iptstatus;
	my $status = "Enabled and Running";

	if (-e "/etc/csf/csf.disable") {
		$status = "<b><font color='red'>Disabled and Stopped</font></b> <form action='$script' method='post'><input type='hidden' name='action' value='enable'><input type='submit' class='input' value='Enable'></form>\n"
	}
	elsif ($config{TESTING}) {
		$status = "<b><font color='red'>Enabled but in Test Mode</font></b> - Don't forget to disable TESTING in the Firewall Configuration";
	}
	elsif ($iptstatus[0] !~ /^Chain LOCALINPUT/) {
		$status = "<b><font color='red'>Enabled but Stopped</font></b> <form action='$script' method='post'><input type='hidden' name='action' value='start'><input type='submit' class='input' value='Start'></form>"
	}
	if (-e "/var/lib/csf/lfd.restart") {$status .= " (lfd restart request pending)"}
	unless ($config{RESTRICT_SYSLOG}) {$status .= "\n<p><font color='red'>WARNING:</font> RESTRICT_SYSLOG is disabled. See SECURITY WARNING in Firewall Configuration</p>\n"}

	my $tempcnt = 0;
	if (! -z "/var/lib/csf/csf.tempban") {
		sysopen (IN, "/var/lib/csf/csf.tempban", O_RDWR);
		flock (IN, LOCK_EX);
		my @data = <IN>;
		close (IN);
		chomp @data;
		$tempcnt = scalar @data;
	}
	my $tempbans = "(Currently: $tempcnt temp IP bans, ";
	$tempcnt = 0;
	if (! -z "/var/lib/csf/csf.tempallow") {
		sysopen (IN, "/var/lib/csf/csf.tempallow", O_RDWR);
		flock (IN, LOCK_EX);
		my @data = <IN>;
		close (IN);
		chomp @data;
		$tempcnt = scalar @data;
	}
	$tempbans .= "$tempcnt temp IP allows)";

	my $permcnt = 0;
	if (! -z "/etc/csf/csf.deny") {
		sysopen (IN, "/etc/csf/csf.deny", O_RDWR);
		flock (IN, LOCK_SH);
		while (my $line = <IN>) {
			chomp $line;
			if ($line =~ /^(\#|\n|\r)/) {next}
			if ($line =~ /$ipv4reg|$ipv6reg/) {$permcnt++}
		}
		close (IN);
	}
	my $permbans = "(Currently: $permcnt permanent IP bans)";

	$permcnt = 0;
	if (! -z "/etc/csf/csf.allow") {
		sysopen (IN, "/etc/csf/csf.allow", O_RDWR);
		flock (IN, LOCK_SH);
		while (my $line = <IN>) {
			chomp $line;
			if ($line =~ /^(\#|\n|\r)/) {next}
			if ($line =~ /$ipv4reg|$ipv6reg/) {$permcnt++}
		}
		close (IN);
	}
	my $permallows = "(Currently: $permcnt permanent IP allows)";

	print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><th align='center' colspan='2'>Firewall Status: $status</th></tr></table><br>\n";

	print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><th align='left' colspan='2'>Server Information</th></tr>";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='servercheck'><input type='submit' class='input' value='Check Server Security'></td><td width='100%'>Perform a basic security, stability and settings check on the server</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='readme'><input type='submit' class='input' value='Firewall Information'></td><td width='100%'>View the csf+lfd readme.txt file</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='logtail'><input type='submit' class='input' value='Watch System Logs'></td><td width='100%'>Watch (tail) various system log files (listed in csf.syslogs)</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='loggrep'><input type='submit' class='input' value='Search System Logs'></td><td width='100%'>Search (grep) various system log files (listed in csf.syslogs)</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='viewports'><input type='submit' class='input' value='View Listening Ports'></td><td width='100%'>View ports on the server that have a running process behind them listening for external connections</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='rblcheck'><input type='submit' class='input' value='Check for IPs in RBLs'></td><td width='100%'>Check whether any of the servers IP addresses are listed in RBLs</form></td></tr>\n";
	if ($config{ST_ENABLE}) {
		print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='viewlogs'><input type='submit' class='input' value='View iptables Log'></td><td width='100%'>View the last $config{ST_IPTABLES} iptables log lines</form></td></tr>\n";
		if ($chart) {
			print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='chart'><input type='submit' class='input' value='View lfd Statistics'></td><td width='100%'>View lfd blocking statistics</form></td></tr>\n";
			if ($config{ST_SYSTEM}) {
				print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='systemstats'><input type='submit' class='input' value='View System Statistics'></td><td width='100%'>View basic system statistics</form></td></tr>\n";
			}
		}
	}
	print "</table><br>\n";

	print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr bgcolor='#FFFFFF'><th align='left' colspan='2'>Upgrade</th></tr>";
	my $retry = 0;
	my $retrytime = 300;
	if (-e "/var/lib/csf/nocheck") {
		open (IN, "<", "/var/lib/csf/nocheck");
		flock (IN, LOCK_SH);
		my $time = <IN>;
		close (IN);
		chomp $time;
		$retry = time - $time;
		if ($retry > $retrytime) {unlink ("/var/lib/csf/nocheck")}
	}
	unless (-e "/var/lib/csf/nocheck") {
		my $url = "https://download.configserver.com/csf/version.txt";
		if ($config{URLGET} == 1) {$url = "http://download.configserver.com/csf/version.txt";}
		my ($status, $text) = &urlget($url);
		my $actv = $text;
		my $up = 0;

		if ($actv ne "") {
			if ($actv =~ /^[\d\.]*$/) {
				if ($actv > $myv) {
					print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='upgrade'><input type='submit' class='input' value='Upgrade csf'></td><td width='100%'><b>A new version of csf (v$actv) is available. Upgrading will retain your settings<br><a href='https://download.configserver.com/csf/changelog.txt' target='_blank'>View ChangeLog</a></b></form></td></tr>\n";
				} else {
					print "<tr bgcolor='#F4F4EA'><td colspan='2'>You are running the latest version of csf. An Upgrade button will appear here if a new version becomes available</td></tr>\n";
				}
				$up = 1;
			}
		}
		unless ($up) {
			sysopen (OUT, "/var/lib/csf/nocheck", O_WRONLY | O_CREAT);
			flock (OUT, LOCK_EX);
			print OUT time;
			close (OUT);
			print "<tr bgcolor='#F4F4EA'><td colspan='2'>Unable to connect to https://download.configserver.com, retry in $retrytime seconds. An Upgrade button will appear here if new version is detected</td></tr>\n";
		}
	} else {
			print "<tr bgcolor='#F4F4EA'><td colspan='2'>Unable to connect to https://download.configserver.com, retry in ".($retrytime - $retry)." seconds. An Upgrade button will appear here if new version is detected</td></tr>\n";
	}
	if (-e "/etc/apf" or -e "/usr/local/bfd") {
		print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='remapf'><input type='submit' class='input' value='Remove APF/BFD'></td><td width='100%'>Remove APF/BFD from the server. You must not run both APF or BFD with csf on the same server</form></td></tr>\n";
	}
	print "</table><br>\n";

	print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><th align='left' colspan='2'>csf - ConfigServer Firewall</th></tr>";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='conf'><input type='submit' class='input' value='Firewall Configuration'></td><td width='100%'>Edit the configuration file for the csf firewall and lfd</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='profiles'><input type='submit' class='input' value='Firewall Profiles'></td><td width='100%'>Apply pre-configured csf.conf profiles and backup/restore csf.conf</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='status'><input type='submit' class='input' value='View iptables Rules'></td><td width='100%'>Display the active iptables rules</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='qallow'><input type='submit' class='input' value='Quick Allow'></td><td width='100%'>Allow IP address <a href='javascript:fillfield(\"allowip\",\"$ENV{REMOTE_ADDR}\")'><img src='$images/ip.png' border='0' alt='$ENV{REMOTE_ADDR}'></a> <input type='text' name='ip' id='allowip' value='' size='18' style='background-color: lightgreen'> through the firewall and add to the allow file (csf.allow).<br>Comment for Allow: <input type='text' name='comment' value='' size='30'></form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='qdeny'><input type='submit' class='input' value='Quick Deny'></td><td width='100%'>Block IP address <input type='text' name='ip' value='' size='18' style='background-color: pink'> in the firewall and add to the deny file (csf.deny).<br>Comment for Block: <input type='text' name='comment' value='' size='30'></form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='qignore'><input type='submit' class='input' value='Quick Ignore'></td><td width='100%'>Ignore IP address <a href='javascript:fillfield(\"ignoreip\",\"$ENV{REMOTE_ADDR}\")'><img src='$images/ip.png' border='0' alt='$ENV{REMOTE_ADDR}'></a> <input type='text' name='ip' id='ignoreip' value='' size='18' style='background-color: lightblue'> in lfd, add to the ignore file (csf.ignore) and restart lfd</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='kill'><input type='submit' class='input' value='Quick Unblock'></td><td width='100%'>Remove IP address <input type='text' name='ip' value='' size='18'> from the firewall (temp and perm blocks)</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='allow'><input type='submit' class='input' value='Firewall Allow IPs'></td><td width='100%'>Edit csf.allow, the IP address allow file $permallows</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='deny'><input type='submit' class='input' value='Firewall Deny IPs'></td><td width='100%'>Edit csf.deny, the IP address deny file $permbans</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='enable'><input type='submit' class='input' value='Firewall Enable'></td><td width='100%'>Enables csf and lfd if previously Disabled</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='disable'><input type='submit' class='input' value='Firewall Disable'></td><td width='100%'>Completely disables csf and lfd</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='restart'><input type='submit' class='input' value='Firewall Restart'></td><td width='100%'>Restart the csf iptables firewall</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='restartq'><input type='submit' class='input' value='Firewall Quick Restart'></td><td width='100%'>Have lfd restart the csf iptables firewall</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='tempdeny'><input type='submit' class='input' value='Temporary Allow/Deny'></td><td width='100%'>Temporarily <select name='do'><option>block</option><option>allow</option></select> IP address <input type='text' name='ip' value='' size='18'> to port(s) <input type='text' name='ports' value='*' size='5'> for <input type='text' name='timeout' value='' size='4'> <select name='dur'><option>seconds</option><option>minutes</option><option>hours</option><option>days</option></select>.<br>Comment: <input type='text' name='comment' value='' size='30'><br>\n(ports can be either * for all ports, a single port, or a comma separated list of ports)</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='temp'><input type='submit' class='input' value='Temporary IP Entries'></td><td width='100%'>View/Remove the <i>temporary</i> IP entries $tempbans</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='grep'><input type='submit' class='input' value='Search for IP'></td><td width='100%'>Search iptables for IP address <input type='text' name='ip' value='' size='18'></form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='sips'><input type='submit' class='input' value='Deny Server IPs'></td><td width='100%'>Deny access to and from specific IP addresses configured on the server (csf.sips)</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='denyf'><input type='submit' class='input' value='Flush all Blocks'></td><td width='100%'>Removes and unblocks all entries in csf.deny (excluding those marked \"do not delete\") and all temporary IP entries (blocks <i>and</i> allows)</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='redirect'><input type='submit' class='input' value='Firewall Redirect'></td><td width='100%'>Redirect connections to this server to other ports/IP addresses</form></td></tr>\n";
	print "</table><br>\n";
	print "<script>function fillfield (myitem,myip) {document.getElementById(myitem).value = myip;}</script>\n";

	if ($config{CLUSTER_SENDTO}) {
		print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
		print "<tr><th align='left' colspan='2'>csf - ConfigServer lfd Cluster</th></tr>";
		print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='callow'><input type='submit' class='input' value='Cluster Allow'></td><td width='100%'>Allow IP address <input type='text' name='ip' value='' size='18' style='background-color: lightgreen'> through the Cluster and add to the allow file (csf.allow)</form></td></tr>\n";
		print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='cdeny'><input type='submit' class='input' value='Cluster Deny'></td><td width='100%'>Block IP address <input type='text' name='ip' value='' size='18' style='background-color: pink'> in the Cluster and add to the deny file (csf.deny)</form></td></tr>\n";
		print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='crm'><input type='submit' class='input' value='Cluster Remove'></td><td width='100%'>Remove IP address <input type='text' name='ip' value='' size='18' style=''> in the Cluster and remove from the deny file (csf.deny)</form></td></tr>\n";
		print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='cping'><input type='submit' class='input' value='Cluster PING'></td><td width='100%'>Ping each member of the cluster (logged in lfd.log)</form></td></tr>\n";
		if ($config{CLUSTER_CONFIG}) {
			if ($ips{$config{CLUSTER_MASTER}} or $ipscidr6->find($config{CLUSTER_MASTER}) or ($config{CLUSTER_MASTER} eq $config{CLUSTER_NAT})) {
				my $options;
				my %restricted;
				if ($config{RESTRICT_UI}) {
					sysopen (IN, "/usr/local/csf/lib/restricted.txt", O_RDWR | O_CREAT) or die "Unable to open file: $!";
					flock (IN, LOCK_SH);
					while (my $entry = <IN>) {
						chomp $entry;
						$restricted{$entry} = 1;
					}
					close (IN);
				}
				foreach my $key (sort keys %config) {
					unless ($restricted{$key}) {$options .= "<option>$key</option>"}
				}
				print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='cconfig'><input type='submit' class='input' value='Cluster Config'></td><td width='100%'>Change configuration option <select name='option'>$options</select> to <input type='text' name='value' value='' size='18'> in the Cluster";
				if ($config{RESTRICT_UI}) {print "<br />\nSome items have been removed with RESTRICT_UI enabled"}
				print "</form></td></tr>\n";
				print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='crestart'><input type='submit' class='input' value='Cluster Restart'></td><td width='100%'>Restart csf and lfd on Cluster members</form></td></tr>\n";
			}
		}
		print "</table><br>\n";
	}

	print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr><th align='left' colspan='2'>lfd - Login Failure Daemon</th></tr>";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='lfdstatus'><input type='submit' class='input' value='lfd Status'></td><td width='100%'>Display lfd status</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='lfdrestart'><input type='submit' class='input' value='lfd Restart'></td><td width='100%'>Restart lfd</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td nowrap><form action='$script' method='post'><input type='hidden' name='action' value='ignorefiles'><select name='ignorefile'>\n";
	print "<option value='csf.ignore'>csf.ignore - IP Blocking</option>\n";
	print "<option value='csf.pignore'>csf.pignore, Process Tracking</option>\n";
	print "<option value='csf.fignore'>csf.fignore, Directory Watching</option>\n";
	print "<option value='csf.signore'>csf.signore, Script Alert</option>\n";
	print "<option value='csf.rignore'>csf.rignore, Reverse DNS lookup</option>\n";
	print "<option value='csf.suignore'>csf.suignore, Superuser check</option>\n";
	print "<option value='csf.mignore'>csf.mignore, RT_LOCALRELAY</option>\n";
	print "<option value='csf.logignore'>csf.logignore, Log Scanner</option>\n";
	print "<option value='csf.uidignore'>csf.uidignore, User ID Tracking</option>\n";
	print "</select> <input type='submit' class='input' value='Edit'></td><td width='100%'>Edit lfd ignore file</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='dirwatch'><input type='submit' class='input' value='lfd Directory File Watching'></td><td width='100%'>Edit the Directory File Watching file (csf.dirwatch) - all listed files and directories will be watched for changes by lfd</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='dyndns'><input type='submit' class='input' value='lfd Dynamic DNS'></td><td width='100%'>Edit the Dynamic DNS file (csf.dyndns) - all listed domains will be resolved and allowed through the firewall</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='templates'><select name='template'>\n";
	foreach my $tmp ("alert.txt","tracking.txt","connectiontracking.txt","processtracking.txt","accounttracking.txt","usertracking.txt","sshalert.txt","webminalert.txt","sualert.txt","uialert.txt","cpanelalert.txt","scriptalert.txt","filealert.txt","watchalert.txt","loadalert.txt","resalert.txt","integrityalert.txt","exploitalert.txt","relayalert.txt","portscan.txt","uidscan.txt","permblock.txt","netblock.txt","queuealert.txt","logfloodalert.txt","logalert.txt") {print "<option>$tmp</option>\n"}
	print "</select> <input type='submit' class='input' value='Edit'></td><td width='100%'>Edit email alert templates. See Firewall Information for details of each file</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='logfiles'><input type='submit' class='input' value='lfd Log Scanner Files'></td><td width='100%'>Edit the Log Scanner file (csf.logfiles) - Scan listed log files for log lines and periodically send a report</form></td></tr>\n";
	print "<tr bgcolor='#FFFFFF'><td><form action='$script' method='post'><input type='hidden' name='action' value='blocklists'><input type='submit' class='input' value='lfd Blocklists'></td><td width='100%'>Edit the Blocklists configuration file (csf.blocklists)</form></td></tr>\n";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='syslogusers'><input type='submit' class='input' value='lfd Syslog Users'></td><td width='100%'>Edit the syslog/rsyslog allowed users file (csf.syslogusers)</form></td></tr>\n";
	print "</table><br>\n";

	if ($config{SMTPAUTH_RESTRICT}) {
		print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
		print "<tr bgcolor='#FFFFFF'><th align='left' colspan='2'>cPanel SMTP AUTH Restrictions</th></tr>";
		print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='smtpauth'><input type='submit' class='input' value='Edit SMTP AUTH'></td><td width='100%'>Edit the file that allows SMTP AUTH to be advertised to listed IP addresses (csf.smtpauth)</form></td></tr>\n";
		print "</table><br>\n";
	}

	if (-e "/usr/local/cpanel/version") {
		print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
		print "<tr bgcolor='#FFFFFF'><th align='left' colspan='2'>cPanel Resellers</th></tr>";
		print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='reseller'><input type='submit' class='input' value='Edit Reseller Privs'></td><td width='100%'>Privileges can be assigned to cPanel Reseller accounts by editing this file (csf.resellers)</form></td></tr>\n";
		print "</table><br>\n";
	}

	print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr bgcolor='#FFFFFF'><th align='left' colspan='2'>Extra</th></tr>";
	print "<tr bgcolor='#F4F4EA'><td><form action='$script' method='post'><input type='hidden' name='action' value='csftest'><input type='submit' class='input' value='Test iptables'></td><td width='100%'>Check that iptables has the required modules to run csf</form></td></tr>\n";
	print "</table><br>\n";

	print "<table align='center' width='95%' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF' style='border:1px solid #990000'>\n";
	print "<tr bgcolor='#FFFFFF'><th align='left' colspan='2'>Development Contribution</th></tr>";
	print "<tr bgcolor='#F4F4EA'><td>We are very happy to be able to provide this and other products for free. However, it does take time for us to develop and maintain them. If you would like to help with their development by providing a PayPal contribution, please <a href='mailto:sales\@waytotheweb.com?Subject=ConfigServer%20Contribution'>contact us</a> for details</td></tr>\n";
	print "</table>\n";
}

unless ($FORM{action} eq "tailcmd" or $FORM{action} eq "logtailcmd" or $FORM{action} eq "loggrepcmd") {
	print "<pre style='font-family: Courier New, Courier; font-size: 12px'>csf: v$myv</pre>";
	print "<p>&copy;2006-2016, <a href='http://www.configserver.com' target='_blank'>ConfigServer Services</a> (Way to the Web Limited)</p>\n";
}
# end main
###############################################################################
# start printcmd
sub printcmd {
	my ($childin, $childout);
	my $pid = open3($childin, $childout, $childout, @_);
	while (<$childout>) {print $_}
	waitpid ($pid, 0);
}
# end printcmd
###############################################################################
# start getethdev
sub getethdev {
	my ($childin, $childout);
	my $cmdpid = open3($childin, $childout, $childout, $config{IFCONFIG});
	my @ifconfig = <$childout>;
	waitpid ($cmdpid, 0);
	chomp @ifconfig;
	foreach my $line (@ifconfig) {
		if ($line =~ /inet.*?($ipv4reg)/) {
			my $ip = $1;
			if (checkip(\$ip)) {$ips{$ip} = 1}
		}
		if ($config{IPV6} and $line =~ /inet6.*?($ipv6reg)/) {
			my ($ip,undef) = split(/\//,$1);
			$ip .= "/128";
			if (checkip(\$ip)) {
				eval {
					local $SIG{__DIE__} = undef;
					$ipscidr6->add($ip);
				};
			}
		}
	}
}
# end getethdev
###############################################################################
# start chart
sub chart {
	my $img;
	my $imgdir = "";
	my $imghddir = "";
	if (-e "/usr/local/cpanel/version") {
		$imgdir = "/";
		$imghddir = "";
	}
	elsif (-e "/usr/local/directadmin/conf/directadmin.conf") {
		$imgdir = "/CMD_PLUGINS_ADMIN/csf/images/";
		$imghddir = "plugins/csf/images/";
		umask(0133);
	}
	if ($config{THIS_UI}) {
		$imgdir = "$images/";
		$imghddir = "/etc/csf/ui/images/";
	}

	sysopen (STATS,"/var/lib/csf/stats/lfdmain", O_RDWR | O_CREAT);
	flock (STATS, LOCK_SH);
	my @stats = <STATS>;
	chomp @stats;
	close (STATS);

	if (@stats) {
		ConfigServer::ServerStats::charts($config{CC_LOOKUPS},$imghddir);
		print ConfigServer::ServerStats::charts_html($config{CC_LOOKUPS},$imgdir);
	} else {
		print "<table style='border: 2px #990000 solid' align='center' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF'>\n";
		print "<tr><td align='center'>No statistical data has been collected yet</td></tr></table>\n";
	}
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
# end chart
###############################################################################
# start systemstats
sub systemstats {
	my $type = shift;
	if ($type eq "") {$type = "load"}
	my $img;
	my $imgdir = "";
	my $imghddir = "";
	if (-e "/usr/local/cpanel/version") {
		if (-e "/usr/local/cpanel/bin/register_appconfig") {
			$imgdir = "csf/";
			$imghddir = "cgi/configserver/csf/";
		} else {
			$imgdir = "/";
			$imghddir = "";
		}
	}
	elsif (-e "/usr/local/directadmin/conf/directadmin.conf") {
		$imgdir = "/CMD_PLUGINS_ADMIN/csf/images/";
		$imghddir = "plugins/csf/images/";
		umask(0133);
	}
	if ($config{THIS_UI}) {
		$imgdir = "$images/";
		$imghddir = "/etc/csf/ui/images/";
	}
	if (defined $ENV{WEBMIN_VAR} and defined $ENV{WEBMIN_CONFIG}) {
		$imgdir = "/csf/";
		$imghddir = "";
	}

	sysopen (STATS,"/var/lib/csf/stats/system", O_RDWR | O_CREAT);
	flock (STATS, LOCK_SH);
	my @stats = <STATS>;
	chomp @stats;
	close (STATS);

	if (@stats > 1) {
		ConfigServer::ServerStats::graphs($type,$config{ST_SYSTEM_MAXDAYS},$imghddir);

		print "<div align='center'><form action='$script' method='post'><input type='hidden' name='action' value='systemstats'><select name='graph'>\n";
		my $selected;
		if ($type eq "" or $type eq "load") {$selected = "selected"} else {$selected = ""}
		print "<option value='load' $selected>Load Average Statistics</option>\n";
		if ($type eq "cpu") {$selected = "selected"} else {$selected = ""}
		print "<option value='cpu' $selected>CPU Statistics</option>\n";
		if ($type eq "mem") {$selected = "selected"} else {$selected = ""}
		print "<option value='mem' $selected>Memory Statistics</option>\n";
		if ($type eq "net") {$selected = "selected"} else {$selected = ""}
		print "<option value='net' $selected>Network Statistics</option>\n";
		if (-e "/proc/diskstats") {
			if ($type eq "disk") {$selected = "selected"} else {$selected = ""}
			print "<option value='disk' $selected>Disk Statistics</option>\n";
		}
		if ($config{ST_DISKW}) {
			if ($type eq "diskw") {$selected = "selected"} else {$selected = ""}
			print "<option value='diskw' $selected>Disk Write Performance</option>\n";
		}
		if (-e "/var/lib/csf/stats/email") {
			if ($type eq "email") {$selected = "selected"} else {$selected = ""}
			print "<option value='email' $selected>Email Statistics</option>\n";
		}
		my $dotemp = 0;
		if (-e "/sys/devices/platform/coretemp.0/temp3_input") {$dotemp = 3}
		if (-e "/sys/devices/platform/coretemp.0/temp2_input") {$dotemp = 2}
		if (-e "/sys/devices/platform/coretemp.0/temp1_input") {$dotemp = 1}
		if ($dotemp) {
			if ($type eq "temp") {$selected = "selected"} else {$selected = ""}
			print "<option value='temp' $selected>CPU Temperature</option>\n";
		}
		if ($config{ST_MYSQL}) {
			if ($type eq "mysqldata") {$selected = "selected"} else {$selected = ""}
			print "<option value='mysqldata' $selected>MySQL Data</option>\n";
			if ($type eq "mysqlqueries") {$selected = "selected"} else {$selected = ""}
			print "<option value='mysqlqueries' $selected>MySQL Queries</option>\n";
			if ($type eq "mysqlslowqueries") {$selected = "selected"} else {$selected = ""}
			print "<option value='mysqlslowqueries' $selected>MySQL Slow Queries</option>\n";
			if ($type eq "mysqlconns") {$selected = "selected"} else {$selected = ""}
			print "<option value='mysqlconns' $selected>MySQL Connections</option>\n";
		}
		if ($config{ST_APACHE}) {
			if ($type eq "apachecpu") {$selected = "selected"} else {$selected = ""}
			print "<option value='apachecpu' $selected>Apache CPU Usage</option>\n";
			if ($type eq "apacheconn") {$selected = "selected"} else {$selected = ""}
			print "<option value='apacheconn' $selected>Apache Connections</option>\n";
			if ($type eq "apachework") {$selected = "selected"} else {$selected = ""}
			print "<option value='apachework' $selected>Apache Workers</option>\n";
		}
		print "</select><input type='submit' class='input' value='Select Graphs'></form></div><br />\n";

		print ConfigServer::ServerStats::graphs_html($imgdir);

		unless ($config{ST_MYSQL} and $config{ST_APACHE}) {
			print "<br>\n<table style='border: 1px #990000 solid' align='center' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF'>\n";
			print "<tr><td align='center'>You may be able to collect more statistics by enabling ST_MYSQL or ST_APACHE in the csf configuration</td></tr></table>\n";
		}
	} else {
		print "<table style='border: 1px #990000 solid' align='center' border='0' cellspacing='0' cellpadding='4' bgcolor='#FFFFFF'>\n";
		print "<tr><td align='center'>No statistical data has been collected yet</td></tr></table>\n";
	}
	print "<p><form action='$script' method='post'><input type='submit' class='input' value='Return'></form></p>\n";
}
# end systemstats
###############################################################################
# start editfile
sub editfile {
	my $file = shift;
	my $save = shift;
	my $extra = shift;
	sysopen (IN, $file, O_RDWR | O_CREAT) or die "Unable to open file: $!";
	flock (IN, LOCK_SH);
	my @confdata = <IN>;
	close (IN);
	chomp @confdata;
	my $max = 80;
	foreach my $line (@confdata) {if (length($line) > $max) {$max = length($line) + 1}}

	print "<form action='$script' method='post'>\n";
	print "<input type='hidden' name='action' value='$save'>\n";
	if ($extra) {print "<input type='hidden' name='$extra' value='$FORM{$extra}'>\n";}
	print "<fieldset><legend><b>Edit $file</b></legend>\n";
	print "<table align='center'>\n";
	print "<tr><td><textarea name='formdata' cols='$max' rows='40' style='font-family: Courier New, Courier; font-size: 12px'>\n";
	foreach my $line (@confdata) {
		$line =~ s/\</\&lt\;/g;
		$line =~ s/\>/\&gt\;/g;
		print $line."\n";
	}
	print "</textarea></td></tr></table></fieldset>\n";
	print "<p align='center'><input type='submit' class='input' value='Change'></p>\n";
	print "</form>\n";
}
# end editfile
###############################################################################
# start savefile
sub savefile {
	my $file = shift;
	my $restart = shift;

	$FORM{formdata} =~ s/\r//g;
	sysopen (OUT, $file, O_WRONLY | O_CREAT) or die "Unable to open file: $!";
	flock (OUT, LOCK_EX);
	seek (OUT, 0, 0);
	truncate (OUT, 0);
	if ($FORM{formdata} !~ /\n$/) {$FORM{formdata} .= "\n"}
	print OUT $FORM{formdata};
	close (OUT);

	if ($restart eq "csf") {
		print "<p>Changes saved. You should restart csf.</p>\n";
		print "<p align='center'><form action='$script' method='post'><input type='hidden' name='action' value='restart'><input type='submit' class='input' value='Restart csf'></form></p>\n";
	}
	elsif ($restart eq "lfd") {
		print "<p>Changes saved. You should restart lfd.</p>\n";
		print "<p align='center'><form action='$script' method='post'><input type='hidden' name='action' value='lfdrestart'><input type='submit' class='input' value='Restart lfd'></form></p>\n";
	}
	elsif ($restart eq "both") {
		print "<p>Changes saved. You should restart csf and lfd.</p>\n";
		print "<p align='center'><form action='$script' method='post'><input type='hidden' name='action' value='restartboth'><input type='submit' class='input' value='Restart csf+lfd'></form></p>\n";
	}
	else {
		print "<p>Changes saved.</p>\n";
	}
}
# end savefile
###############################################################################
# start urlget
sub urlget {
	my $url = shift;
	my $file = shift;
	my $quiet = shift;
	my $status;
	my $text;
	($status, $text) = $urlget->urlget($url,$file,$quiet);
	return ($status, $text);
}
# end urlget
###############################################################################

1;
