(function(e) {
    function u() {
        $("h1, h2").each(function() {
            var e = $(this);
            var t = e.nextUntil("h1, h2");
            o.add({
                id: e.prop("id"),
                title: e.text(),
                body: t.text()
            }) 
        })
    }

    function a() {
        n = $(".content");
        r = $(".dark-box");
        i = $(".search-results");
        $("#input-search").on("keyup", f)
    }

    function f(e) {
        c();
        i.addClass("visible");
        if (e.keyCode === 27) this.value = "";
        if (this.value) {
            var t = o.search(this.value).filter(function(e) { 
                return e.score > 1e-4
            });
 
            if (t.length) {
                i.empty();
                $.each(t, function(e, t) { 
                    i.append("<li><a href='#" + t.ref + "'>" + $("#" + t.ref).text() + "</a></li>")
                });
                l.call(this)
            } else {
                i.html('<li>No Results Found for "' + this.value + '"</li>')
            }
        } else {
            c();
            i.removeClass("visible")
        }
    }

    function l() {
        if (this.value) n.highlight(this.value, s)
    }

    function c() {
        n.unhighlight(s)
    }
    var t = $(e);
    var n, r, i;
    var s = {
        element: "span",
        className: "search-highlight"
    };

      var o = lunr(function () {
            // use the language (de)
            this.ref("id");
 
            this.use(lunr.da);
            this.use(lunr.de);
            this.use(lunr.du);
            this.use(lunr.es);
            this.use(lunr.fi);
            this.use(lunr.fr);
            this.use(lunr.hu);
            this.use(lunr.it);
            this.use(lunr.jp);
            this.use(lunr.no);
            this.use(lunr.pt);
            this.use(lunr.ro);
            this.use(lunr.ru);
            this.use(lunr.sv);
            this.use(lunr.tr);

            // then, the normal lunr index initialization
            this.field('title', { boost: 10 })
            this.field('body')
        });

    $(u);
    $(a)
})(window)
