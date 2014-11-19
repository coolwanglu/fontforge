#Needs: fonts/futuraBT-Medium-2048EMSize.cff

import os, sys, shutil, tempfile, fontforge;

#results = tempfile.mkdtemp('.tmp','fontforge-test-')
resultDir = "results"
if (not os.path.exists(resultDir)):
    os.mkdir(resultDir)



print "This font has Em-size of 2048, and there will be a mismatch between glyph size and em-size once converted to ttf if no bugfix"
f1 = fontforge.open(os.path.join("fonts", "futuraBT-Medium-2048EMSize.cff"))
f1.generate(os.path.join(resultDir, "futuraBT-Medium-2048EMSize.ttf"), flags=("apple",));
f1.close()

'''
shutil.rmtree(results)
'''
