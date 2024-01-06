PowerShell Cmdlet Anatomy

Tuesday, October 24, 2023

8:20 PM

 

 

In PowerShell, the commands that you run are called cmdlets. Typically, cmdlets do one thing really well. The idea is to have multiple cmdlets that all do one thing really well and chain them together in a \"pipeline\".

 

PowerShell cmdlet names should conform to a standard -- Verb-Noun. The idea behind this is that a cmdlet should be very clear about what it does. This is important, so that the user can be sure of the nature of the cmdlet.

 

For example, a cmdlet that starts with a Get- verb, you can be confident that this is not a destructive cmdlet. However, a cmdlet that starts with the verb Remove-, you can be sure that this is a destructive cmdlet and should be very careful with how you use it.

 

[Approved Verbs for PowerShell Commands - PowerShell \| Microsoft Learn](https://learn.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7.3&ref=benheater.com)

 

PowerShell uses the term verb to describe a word that implies an action even if that word is not a standard verb in the English language. For example, the term New is a valid PowerShell verb name because it implies an action even though it is not a verb in the English language
