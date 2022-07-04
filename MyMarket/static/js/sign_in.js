const tween1 = KUTE.fromTo(
    '#top-right-1',
    { path: '#top-right-1'},
    { path: '#top-right-2'},
    { repeat:Infinity, duration:3000, yoyo:true },
    
);
tween1.start();

const tween2 = KUTE.fromTo(
    '#bottom-left-1',
    { path: '#bottom-left-1'},
    { path: '#bottom-left-2'},
    { repeat:Infinity, duration:3000, yoyo:true },
    
);
tween2.start();