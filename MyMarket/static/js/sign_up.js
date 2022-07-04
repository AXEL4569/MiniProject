const tween1 = KUTE.fromTo(
    '#top-left-1',
    { path: '#top-left-1'},
    { path: '#top-left-2'},
    { repeat:Infinity, duration:3000, yoyo:true },
    
);
tween1.start();

const tween2 = KUTE.fromTo(
    '#bottom-right-1',
    { path: '#bottom-right-1'},
    { path: '#bottom-right-2'},
    { repeat:Infinity, duration:3000, yoyo:true },
    
);
tween2.start();