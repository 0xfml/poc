### Description

Quorum 2.03 and earlier stores all user information in .dat files on the local disk. This can lead to leakages of information when access to the file system is permitted or when used in conjunction with the LFI. 

### Vulnerability type

Cleartext Credential Storage

### Vendor
NCH Software

### Affected versions
Quorum 2.03 and earlier

### Attack type

Local

### Authenticated

Yes

### Attack vectors
Quorum stores all registered user information in a .dat file on the local disk. The files contain cleartext username, password and auth level.
```
C:\ProgramData\NCH Software\Quorum\Users\{user}.dat
```
### Link

https://www.nch.com.au/conference/index.html
