loadFile = (event) => {
    var image = document.getElementById('current-avatar');
    image.src = URL.createObjectURL(event.target.files[0]);
};
