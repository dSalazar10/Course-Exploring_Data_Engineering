# To have launchd start cassandra now and restart at login:
brew services start cassandra
# Or, if you don't want/need a background service you can just run:
#cassandra -f