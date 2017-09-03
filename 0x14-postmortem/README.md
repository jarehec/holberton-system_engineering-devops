[![](http://i.imgur.com/GOuMboG.png)](https://the-para.site)
---
# August 14th 2017 Incident Report
![](http://i.imgur.com/BDvOLHe.jpg)
### Issue Summary
From 02:42 PDT on Monday August 14 2017 to 08:22 August 14 our servers were attacked. Multiple malicious files were uploaded to the downloads page on our website. If you have downloaded and executed files from our website in this time period your information is at risk of being stolen. It may not seem dangerous but the malicious program steals saved login credentials stored on your web browser. We recommend that users immediately change all off their passwords to prevent their information from being stolen. The hacker used a brute-forcing program to successfully gain access to our server. We have changed our method of accessing the server to a significantly more secure process in response to this event.

## Timeline
* [02:42] Monitoring service alerts us about an unusually high amount of network traffic.
* [03:02] - Monitoring service notifies us that one of our servers was being accessed from an unknown IP address.
* [03:42] - Several files updated in the upload directory on our server.
* [04:20] - We notice 3 HTML files edited. The 'sign in' URL redirected toward a fake login page. (`index.html, about.html, downloads.html`)
* [04:22] - We change the password to our server.
* [04:30] - Copied the files the hacker uploaded for later examination.
* [05:11] - We stop the nginx process on web servers and verify that no unknown users have access.
* [05:14] - Alpine Linux is installed on our servers.
* [05:30] - Use Puppet and Fabric scripts to setup and configure our web servers and load-balancers.
* [06:40] - Configure servers to only accept users that have a private key.
* [06:42] - Verify that users cannot login without the private key. (Success)
* [06:45] - Updated firewall rules.
* [06:50] - Penetration test our server to make sure that the new configuration is secure.
* [08:22] - Restarted web server
* [08:30] - Examine files that were uploaded by the hacker.

## Root Cause
The main problem was the configuration of our server. It used the password: `Username1` which is extremely insecure. Also only the password was needed to gain access. The password was changed to a randomly generated string. We also added an extra layer of security by making an RSA private key necessary to access to our servers.

## Remediation AND Prevention
To prevent future attacks we installed a clean copy of Alpine Linux instead of Ubuntu as it is more secure. Suspicious IPs are now blocked from connecting to our servers.
