

















0. A file has been removed from the working tree, however the file was not removed from the repository. Find out what this file was and remove it.

```
git status
git rm <filename>
```

1. A file has accidentally been added to your staging area, find out which file and remove it from the staging area.  *NOTE* Do not remove the file from the file system, only from git.

```
git status
git rm -cache <filename>
```


