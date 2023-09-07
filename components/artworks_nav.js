// see https://www.geeksforgeeks.org/read-json-file-using-javascript/
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise?retiredLocale=de
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions?retiredLocale=de
// https://stackoverflow.com/questions/29516390/how-can-i-access-the-value-of-a-promise


async function getModelNames() {
    const jsonPromise = await fetch("/schattenorigami/artworks.json")
        .then((res) => {
        return res.json();
    });

    return jsonPromise["model_names"];
}

function getHtmlStr(model_names) {
    const docTitle = document.title;

    var htmlStr = '';
    for (const name of model_names) {
        const nameSnake = name.toLowerCase().replaceAll(' ', '_');
        const artworkPagePath = '/schattenorigami/artwork_pages/' + nameSnake + '.html';
        const page = docTitle.split('-').pop(); 

        var activeStr = '';
        if (name === page) {
            activeStr = ' class="uk-active"'
        }
        htmlStr += '<li' + activeStr + '><a href="' + artworkPagePath + '">' + name + '</a></li>\n';
    }

    return htmlStr;
}

class ArtworksNav extends HTMLElement {
    constructor() {
        super();
    }

    async connectedCallback() {
        const model_names = await getModelNames()
        const htmlStr = getHtmlStr(model_names);      
        
        this.innerHTML = `
        <div class="my-sidebar-left uk-padding-small uk-visible@xl">
            <ul class="uk-nav uk-nav-default">
                <li class="uk-nav-header uk-text-center">Models</li>
                <li class="uk-nav-divider"></li>
        ` + htmlStr + `</ul></div>`;
    }
}

customElements.define('my-artworks-nav', ArtworksNav);



/*const artworkNames = ['Avicularia alata', 'Redback Spider',  'Simple Catgirl', 'Simple Demon', 'Tiny Turt',];

class ArtworksNav extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        const artworkNames = GetArtworkNames()
        console.log(artworkNames)
        const docTitle = document.title;

        var htmlStr = '';

        for (const name of artworkNames) {
            var activeStr = '';
            if (name === docTitle.split('-').pop()) {
                activeStr = ' class="uk-active"'
            }
            htmlStr += '<li' + activeStr + '><a href="/schattenorigami/' + name.toLowerCase().replace(' ', '_') + '.html">' + name + '</a></li>\n';
        }

        this.innerHTML = `
        <div class="my-sidebar-left uk-padding-small uk-visible@xl">
            <ul class="uk-nav uk-nav-default">
                <li class="uk-nav-header uk-text-center">Models</li>
                <li class="uk-nav-divider"></li>
        ` + htmlStr + `</ul></div>`;
    }
}
*/


/*
<div class="my-sidebar-left uk-padding-small uk-visible@xl">
    <ul class="uk-nav uk-nav-default">
        <li class="uk-nav-header uk-text-center">Models</li>
        <li class="uk-nav-divider"></li>
        <li><a href="avicularia_alata.html">Avicularia alata</a></li>
        <li><a href="redback_spider.html">Redback Spider</a></li>
        <li><a href="simple_demon.html">Simple Demon</a></li>
        <li class="uk-active"><a href="tiny_turt.html">Tiny Turt</a></li>
    </ul>
</div>
*/