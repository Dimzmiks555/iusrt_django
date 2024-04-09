let filter_button = document.querySelector('#filter_button') 



if (filter_button) {

    let type_filter = document.querySelector('.type_filter') 
    let status_filter = document.querySelector('.status_filter select') 
    let type = 0, status = status_filter.value;
    



    type_filter.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', (e) => {
                type = +e.target.dataset.id
                type_filter.querySelectorAll('a').forEach(link => {
                    link.classList.remove("selected")
                })
                e.target.classList.add("selected")
        })
    })

    status_filter.addEventListener('change', (e) => {
        if (e.target.value != '') {
            if (e.target.value == '1') {
                status = 1
            } else {
                status = 0
            }
        } else {
            status = ''
        }
    })

    filter_button.addEventListener('click', (e) => {
        let url = new URL(window.location.href);
        url.searchParams.set('page', '1');
        status != "none" && url.searchParams.set('status', status);

        if (type > 0) {
            url.searchParams.set('type', type);
        } else {
            url.searchParams.set('type', '');
        }
 
        window.location.href = url 
    })
}

