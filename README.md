# iOS-imageset

**iOS-imageset** is a simple python script for helping iOS-App designer generate @1x@2x@3x png imageset.

Note that **iOS-imageset** depends on [PIL](http://www.pythonware.com/products/pil/),install it before using.

You can follow either follow the instructions below or visit [my blog](http://jcggg.me/2015/09/26/iOS%E5%88%87%E5%9B%BE%E6%89%93%E5%8C%85%E8%84%9A%E6%9C%AC/):

```
1. python imageset.py -d(or --dir) [directory]:
    make imagesets from all png files in directory
2. python imageset.py [filepath]:
    make one imageset from the specific png file at filepath
```

With just one command, you can generate imagesets from your png files(which stand for @3x size) and simply drag them into `Images.xcassets` of your Xcode project.

Enjoy it and contact me for any problems!
