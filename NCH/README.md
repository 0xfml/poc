# NCH Software Vulnerability Advisories

## Affected Software
**IVM Attendant <5.12** - RCE, Path Traversal + Arbitrary File Delete, Multiple XSS <br>
**Axon PBX <2.22** - Path Traversal +Arbitrary File Delete, Multiple XSS <br>
**Quorum <2.03** - Path Traversal + Arbitrary File Delete, Multiple XSS, Cleartext Credential Storage <br>
**FlexiServer <6.00** - Path Traversal <br>
**WebDictate <2.13** - Path Traversal, XSS <br>
**Reflect CRM <3.01** - Cleartext Credential Storage <br>

_note: all vulnerabilities outlined were tested on up-to-date versions as of Q2 2021, initial vendor responses indicated no fixes would be applied however this may change. Earlier versions were not available for testing so are assumed vulnerable._

## Disclosure Timeline

30/03/21 - Vulnerabilities identified and verified <br>30/03/21 - Issues reported via 'Report a bug' web form <br>30/03/21 - Automated response from the support line. <br>
01/04/21 - Response from vendor support asking for more information to pass to dev team <br>02/04/21 - Reply stating that I will supply a formal report for easier understanding <br>05/04/21 - Delivery of a formal report outlining all findings <br>
06/04/21 - Acknowledgment of receipt, support forwarding to upper management <br>
15/04/21 - Follow up to offer responses to any queries <br>
16/04/21 - Support response stating issues are being fixed/customers notified <br>
16/04/21 - Website updated with included security risk outlines on affected products <br>
20/07/21 - Requested CVE IDs through MITRE <br>



## Vendor Fixes

Applied security notices to some of the products, others were labeled as legacy or removed.

``` 
Security Notice: If you setup an admin on IVM the Admin can install other programs
or access all files on the computer running like any admin can. Do not setup a weblet
admin for someone who you would not be willing to be admin of the PC.
```
The overall support experience reporting the issues was positive and responsive however it appears theres no high priority for fixing security related issues.

## Recommended Fix
Use something else

## Notes
I wasnt able to find any login bypasses to make any of these vulns unauthenticated. All the applications seem to be using the same underlying web server components, including what appeared to be a simple strcmp like call against the login details kept in registry or on disk.
