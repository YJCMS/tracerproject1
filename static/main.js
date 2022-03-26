Dropzone.autoDiscover = false;

const myDropzone = new Dropzone("#my-dropzone", {
    url: "upload/",
    maxFiles: 1,
    maxFilesize: 10,
    acceptedFiles: '.png, .jpg'
})