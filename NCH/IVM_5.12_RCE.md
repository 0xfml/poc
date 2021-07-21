### Description

An authenticated user can gain remote code execution in NCH IVM attendant through the plugin upload functionality. The plugin functionality inherits a trivial zip-slip style zip extraction path traversal where the designed file is a windows executable packed into a zip file. Code execution can be achieved in two ways; the first being a typical exe drop into the users startup folder, and the second being a drop to anywhere on the disk and creating a Out-Going Message within IVM to run the application on a failed SIP call. The 'AutoDial' web function can then be used with this OGM to make an outbound test call to a non-existent number thus triggering the rule and subsequently the executable. 

### Vulnerability type

Remote Code Execution

### Vendor
NCH Software

### Affected versions

IVM Attendant v5.12 and earlier

### Attack type

Remote

### Authenticated

Yes

### Attack vectors

An authenticated attacker must package a path traversal zip file payload containing an executable file and upload via the plugin upload function. Triggering the payload can be done in 2 ways, as described above.

### Link

https://www.nch.com.au/ivm/index.html
