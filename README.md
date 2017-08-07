# How to demo Fugue from this repo

Have a few processes already running. The VpcOnly.lw composition is useful for this. Also have Fugue Composer available.

## Start with CLI. This is how you as a user can communicate with the Conductor.
- run `fugue status` and explain what a process is, and point out how they run in different accounts and how last message shows their state
- run `fugue account list` to show the different accounts and how you can nickname them
- run `fugue status <alias|FID>` and explain how all resources are encapsulated in a process
- run `fugue history <alias|FID>` and explain that user jobs, orchestration jobs, and enforcement jobs are all happening
- explain that we want to provision a new workload and we'll do so with `fugue run` but first let's see what we're going to be provisioning

## Switch to Composer
- show FugueDemo.lw and explain that the diagram is based on the code
- violate a policy by changing region to other than us-west-* and show how clear the error is and how it saves developers time in not having to chase down current rule details
- optional, change instance type to M4_large and just point out that any AWS resource can be validated
- save the fixed composition so the diagram is back

## Back to CLI
- run the FugueDemo.lw composition explaining aliases and, optionally, target an account 
- explain the compilation/validation process and how the composition is uploaded and becomes the Conductor's instructions

## Switch to your editor with FugueDemo.lw open
- talk in some more detail about imports, libraries, and abstractions
- show the Network example, quickly highlight that the rest of the composition is based on declarative records
- show an example validation and how straightforward they are to code, talk about DevSecOps and vending "blessed" policies
- bring up App.lw and explain how the FugueDemo.lw composition is quite verbose, but as you want to re-use common workload patterns, 
or provide them as "self-service catalogs" to your organization, you can create function that modularizes that workload. Point out the Backend.new record in App.lw, just three fields.
- show App.lw in Composer so they can see how its the same workload 

Switch to AWS Web Console
- talk about conductor enforcement, generally how it works and such
- go to a security group and make a change
- go back to the editor and show the security group record in FugueDemo.lw pointing out how its the conductor's source of truth
- talk, probably a lot, to fill in the gap before the enforcement tick happens
- show the security group being fixed


