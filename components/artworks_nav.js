const artworkNames = ['Avicularia alata', 'Redback Spider', 'Simple Demon', 'Tiny Turt'];

class ArtworksNav extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        const docTitle = document.title;

        var html_str = '';

        for (const name of artworkNames) {
            var active_str = '';
            if (name === docTitle.split('-').pop()) {
                active_str = ' class="uk-active"'
            }
            html_str += '<li' + active_str + '><a href="/schattenorigami/' + name.toLowerCase().replace(' ', '_') + '.html">' + name + '</a></li>\n';
        }

        this.innerHTML = `
        <div class="my-sidebar-left uk-padding-small uk-visible@xl">
            <ul class="uk-nav uk-nav-default">
                <li class="uk-nav-header uk-text-center">Models</li>
                <li class="uk-nav-divider"></li>
        ` + html_str + `</ul></div>`;
    }
}

customElements.define('my-artworks-nav', ArtworksNav);

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