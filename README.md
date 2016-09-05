# ber-kit
Toolkit used to manage invisible rolling upgrades of systems running atop a Marathon/Mesosphere stack. 
This is required until Marathon issue is resolved: https://github.com/mesosphere/marathon/issues/2414  

Original sources:  
* https://groups.google.com/forum/#!topic/marathon-framework/MBt6Qf0vH-A  
* https://gist.github.com/pradeepchhetri/2eafdc75d89236018cbf9e6e57bc1885

# Tools
## drain
Drain tasks from hosts running on specified IP addresses, so that you can safely perform maintenance on them. This works by addings the `UNLIKE` constraint for you.

Usage:
```
ber-kit drain --host http://marathon-us-east-1-staging.hub.bitbrew.com --urls 10.30.40.50,10.30.40.51
```

## undrain
Once your migrations and rollovers are complete you need to cleanup and remove the temporary `UNLIKE` constraint.

Usage:
```
ber-kit drain --host http://marathon-us-east-1-staging.hub.bitbrew.com --urls 10.30.40.50,10.30.40.51
```
