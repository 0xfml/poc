### Description

An authenticated user can view any file on the remote system via path traversals in the syslog function. This is dependent on the running context of the application. This can also be used to view credential files of other NCH applications often stored in `\ProgramData\NCH Software\`.

### Vulnerability type

Directory Traversal

### Vendor
NCH Software

### Affected versions

WebDictate 2.13 and earlier

### Attack type

Remote

### Authenticated

Yes

### Attack vectors

`HOST/logprop?file=/../../../../../../Windows/win.ini` (read)

### Link

https://www.nch.com.au/webdictate/index.html
