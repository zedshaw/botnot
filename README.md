botnot
======

What if monit was a botnet?  Just a random idea I had while waiting for the
subway in NYC.

What I want this to do is have a simple way to "infect" a bunch of machines I
need monitored with a bot that hits a command and control server (cctrl) to
find out what other bots are running.  These bots then check each other's
running accessible ports and if any go down they simply send an email to
whoever the cctrl server says to contact.  The bots are self-configuring and
simply know how to check that everything with a port should be running, the
disk isn't full, and the memory isn't full, processes are still running, etc.

Because the cctrl server will get data on each bots ports over time, it will
know the deltas of port changes, memory changes, disk, etc. and can 

This isn't meant to be an insanely scalable notifications system, but just
something someone with a few machines can install very quickly and get
notifications by email when things go wrong.

It's also a fun hack for me to learn ssh programming with paramiko and get
better at using gevent.

