
async function getModelList() {
    const jsonPromise = await fetch("./artworks.json")
        .then((res) => {
        return res.json();
    });

    return jsonPromise["model_list"];
}


function getModelCardHtml(model) {
    const date = model["dates"][0];
    const dateNum = model["dates_num"][0];
    const name = model["name"];
    const cp = model["cps"][0];
    const diagram = model["diagrams"][0];
    const imgPath = model["img_paths"][0][0];
    const artworkPage = model["artwork_page_path"];
    
    var filterStr = '';
    var iconsStr = '';
    if (diagram) {
        filterStr += `tag-diagrams `
        iconsStr += `<img src="assets/icons/diagrams_icon.svg" width="35" uk-svg></img>`
    }
    if (cp) {
        filterStr += `tag-CP tag-test`;
        iconsStr += `<img src="assets/icons/cp_icon.svg" width="35" uk-svg></img>`
    }


    htmlStr = `
        <li data-date="` + dateNum + `" data-name="` + name + `" class="` + filterStr + `">
            <div class="uk-card uk-card-default uk-link-toggle uk-transition-toggle uk-inline-clip uk-card-hover">
                <a href="` + artworkPage + `" class="uk-link-muted">
                    <div class="uk-card-media-top uk-transition-scale-up uk-transition-opaque">
                        <img class="my-img-square" src="`+ imgPath + `" alt="">
                    </div>
                    <div class="uk-card-body">
                        <h3 class="uk-card-title">` + name + `</h3>
                        ` + date + ` 
                    </div>
                </a>
                <div class="uk-position-top-right uk-padding-small"> 
                    ` + iconsStr + `
                </div>
            </div>
        </li>

    `
    return htmlStr;
}

class Gallery extends HTMLElement {
    constructor() {
        super();
    }

    async connectedCallback() {
        const modelList = await getModelList();
        var allCards = ''
        for (const model of modelList) {
            allCards += getModelCardHtml(model);
        }

        this.innerHTML += `<ul class="js-filter uk-grid-small uk-child-width-1-2@s uk-child-width-1-3@m uk-child-width-1-4@l uk-text-center" 
                            uk-grid uk-height-match="target: > li > .uk-card">
        ` + allCards +
        `</ul>`
    }
}

customElements.define('my-gallery', Gallery);