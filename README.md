### Fugue Demo Composition
This version of FugueDemo.lw is the usual workload but with a few new things that help us showcase policies.

There is now an ```EBS Instance``` that attaches to the ```LaunchConfiguration```. It has an ```EC2.Volume``` configured and there is a corresponding validation that its encrypted.

There are two policy files, one with SSH and one without. For myself, I've been using the one *with* SSH for conductor side. That way in a demo I can allow SSH to the ASG and it will compile fine, but then the conductor will reject it. The case being this particular target conductor is only for production.