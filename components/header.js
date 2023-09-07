class Header extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        const docTitle = document.title;
        const linksList = ['Artworks', 'About', 'Commissions'];

        var html_str = '';

        for (const name of linksList) {
            var active_str = '';
            if (name === docTitle.split('-')[0]) {
                active_str = ' uk-active'
            }
            html_str += '<li class="uk-text-bold' + active_str + '"><a href="/schattenorigami/' + name.toLowerCase() + '.html">' + name + '</a></li>';
        }

        this.innerHTML = `
            <nav class="uk-visible@s uk-background-top-right uk-background-cover uk-margin-small-bottom uk-background-muted" style="background-image: url(/schattenorigami/assets/triangulated_navbar_gradient.png)" uk-navbar uk-sticky>
                <ul id="navbar" class="uk-navbar-nav uk-background-muted"">
                    <li>
                        <a class="uk-logo uk-margin-left" href="/schattenorigami/index.html">
                            <img src="/schattenorigami/assets/logo_title.svg" width="120" uk-svg></img>
                        </a>
                    </li>
            ` + html_str + `</ul></nav>`;
    }
}

customElements.define('my-header-navbar', Header);


/*this.innerHTML = `
<header>
<!--
    <nav class="uk-navbar-container uk-margin-small-bottom" uk-navbar uk-sticky>
--> 
    <nav class="uk-background-top-right uk-background-cover uk-margin-small-bottom uk-background-muted uk-background-image@s" style="background-image: url(/schattenorigami/assets/triangulated_navbar_gradient.png)" uk-navbar uk-sticky>
        <ul id="navbar" class="uk-navbar-nav uk-background-muted"">
            <li>
                <a class="uk-logo uk-margin-left" href="/schattenorigami/index.html">
                    <img src="/schattenorigami/assets/logo_title_120.png">
                </a>
            </li>

            <li id="my-navbar-artworks-link" class="uk-text-bold">
                <a href="/schattenorigami/artworks.html">
                    artworks
                </a>
            </li>

            <li id="my-navbar-about-link" class="uk-text-bold">
                <a href="/schattenorigami/about.html">
                    about
                </a>
            </li>

            <li id="my-navbar-comissions-link" class="uk-text-bold">
                <a href="/schattenorigami/commissions.html">
                    commissions
                </a>
            </li>

            <li id="my-navbar-test-link" class="uk-text-bold">
                <a href="/schattenorigami/test.html">
                    <span class="my-comment">
                        test
                    </span>
                </a>
            </li>
        </ul>
    </nav>
</header>
`;*/
