async function getModelNames() {
    const jsonPromise = await fetch("/schattenorigami/artworks.json")
        .then((res) => {
        return res.json();
    });

    return jsonPromise["model_names"];
}

function getModelsHtmlStr(model_names) {
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



class MobileNav extends HTMLElement {
    constructor() {
        super();
    }

    async connectedCallback() {
        const docTitle = document.title;
        const linksList = ['Artworks', 'About', 'Commissions'];

        const modelNames = await getModelNames()
        const modelsHtmlStr = getModelsHtmlStr(modelNames);  


        var mainNavStr = '';

        for (const name of linksList) {
            var activeStr = '';
            if (name === docTitle.split('-')[0]) {
                activeStr = ' uk-active'
            }
            mainNavStr += '<li class="uk-text-bold' + activeStr + '"><a href="/schattenorigami/' + name.toLowerCase() + '.html">' + name + '</a></li>';
        }


        this.innerHTML = `
            <nav class="uk-hidden@s uk-background-top-right uk-background-cover uk-margin-small-bottom uk-background-muted" style="background-image: url(/schattenorigami/assets/triangulated_navbar_gradient.png)" uk-navbar uk-sticky>
                <ul class="uk-navbar-nav uk-background-muted"">
                    <li>
                        <a class="uk-logo uk-margin-left" href="/schattenorigami/index.html" uk-toggle="target: #offcanvas-nav-primary">
                            <img src="/schattenorigami/assets/logo_title_120.png">
                        </a>
                    </li>
                </ul>
            </nav>

            <div id="offcanvas-nav-primary" uk-offcanvas="overlay: true">
                <div class="uk-offcanvas-bar uk-flex uk-flex-column">
                    <button class="uk-offcanvas-close" uk-close></button>

                    <ul class="uk-nav uk-nav-primary uk-nav-center uk-margin-auto-vertical"> 
                        <li>
                            <a class="uk-logo" href="/schattenorigami/index.html">
                                <img src="/schattenorigami/assets/logo_title_120.png">
                            </a>
                        </li>`
                        + mainNavStr + `
                        <li class="uk-parent">
                            <ul class="uk-nav-sub">
                                <li class="uk-nav-header uk-margin-top">Models</li>
                                <li class="uk-nav-divider"></li>`
                                + modelsHtmlStr + `
                            </ul>
                        </ul>
                        
                </div>
            </div>
        `
    }
}

customElements.define('my-mobile-nav', MobileNav);