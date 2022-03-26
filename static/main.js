Dropzone.autoDiscover = false;

const myDropzone = new Dropzone("#my-dropzone", {
    url: "upload/",
    maxFiles: 1,
    maxFilesize: 10,
    acceptedFiles: '.png, .jpg'
})

const myDropzone2 = new Dropzone("#my-dropzone2", {
    url: "upload2/",
    maxFiles: 1,
    maxFilesize: 100,
    acceptedFiles: '.mp4'
})