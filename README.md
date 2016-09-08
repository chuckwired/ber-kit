# ber-kit
Toolkit used to manage invisible rolling upgrades of systems running atop a Marathon/Mesosphere stack.
This is required until Marathon issue is resolved: https://github.com/mesosphere/marathon/issues/2414  

Original sources:  
* https://groups.google.com/forum/#!topic/marathon-framework/MBt6Qf0vH-A  
* https://gist.github.com/pradeepchhetri/2eafdc75d89236018cbf9e6e57bc1885

# Usage
## drain
Drain tasks from hosts running on specified IP addresses, so that you can safely perform maintenance on them. This works by addings the `UNLIKE` constraint for you.

Usage:
```
ber-kit drain --host http://marathon.example.com:8080 --urls 10.30.40.50,10.30.40.51
```

## undrain
Once your migrations and rollovers are complete you need to cleanup and remove the temporary `UNLIKE` constraint.
You can also use this to rollback should your upgrade fail.

Usage:
```
ber-kit undrain --host http://marathon.example.com:8080 --urls 10.30.40.50,10.30.40.51
```

# Testing
You can run the built-in tests by running:
```
nosetests /path/to/ber-kit
```

You can install this by running `pip install nose`.  

# Licensing
Licensed under the GNU GPLv3 License. See `LICENSE`
