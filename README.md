In this program, we use opencv to apply sepia effect to a live webcam feed.
For this we start recording, extract each recording frame-by-frame and process it.
The frame obtained is a 3-D matrix where each dimension represents height, width and channels (RGB) respetively.
In the processing step, we first flatten the image to obtain a 1-D array.
This is done because numpy processes faster on 1-D arrays than n-D arrays.
Now we run a for loop with step 3 to get sets of coloured pixels and then multiply this pixel matrix with sepia matrix.
The array is then reshaped to its original size and the frame is displayed.
