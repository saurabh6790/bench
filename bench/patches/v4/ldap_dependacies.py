from playbooks.install import get_distribution_info
import subprocess

def execute():
	dist_name, dist_version = get_distribution_info()
	
	supported_dists = {
		'ubuntu': {
			"versions": [14, 15, 16],
			"dependacies": ["libsasl2-dev", "python-dev", "libldap2-dev", "libssl-dev"],
			"installer_program": "sudo apt-get install"
		},
		'debian': {
			"versions": [7,8],
			"dependacies": ["libsasl2-dev", "python-dev", "libldap2-dev", "libssl-dev"],
			"installer_program": "sudo yum install"
		},
		'centos': {
			"versions": [7],
			"dependacies": ["python-devel", "openldap-devel"],
			"installer_program": "sudo apt-get install"
		},
	}
	
	try:
		if dist_name in supported_dists:
			if float(dist_version) in supported_dists[dist_name]["versions"]:
				subprocess.check_call("{0} {1}".format(supported_dists[dist_name]["installer_program"],
				', '.join(supported_dists[dist_name]["dependacies"])), shell=True)

				subprocess.check_call("sudo pip install python-ldap", shell=True)

	except Exception:
		print """" Sorry, the installer doesn't support {0} {1}. Aborting installation!
			Please install LDAP dependencies manually """.format(dist_name, dist_version)
			