window.addEventListener("load", function() {

    let status = document.getElementsByName('status')[0];

    if (typeof status != 'undefined') {
        status.addEventListener('change', (event) => {
            if (status.checked) {
                status.value = true;
            } else {
                status.value = false;
            }
        });
    }

});