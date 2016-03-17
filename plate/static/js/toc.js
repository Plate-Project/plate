(function(e) {
    function r() {
        setTimeout(function() {
            toc.setOption("showEffectSpeed", 180)
        }, 50)
    }
    var t = function() {
        $(".tocify-wrapper").removeClass("open");
        $("#nav-button").removeClass("open")
    };
    var n = function() {
        console.log(e);

        e.toc = $("#toc").tocify({
            selectors: "h1, h2",
            extendPage: false,
            theme: "none",
            smoothScroll: false,
            showEffectSpeed: 0,
            hideEffectSpeed: 100,
            ignoreSelector: ".toc-ignore",
            highlightOffset: 60,
            scrollTo: -1,
            scrollHistory: true,
            hashGenerator: function(e, t) {
                return t.prop("id")
            }
        }).data("toc-tocify");
        $("#nav-button").click(function() {
            $(".tocify-wrapper").toggleClass("open");
            $("#nav-button").toggleClass("open");
            return false
        });
        $(".page-wrapper").click(t);
        $(".tocify-item").click(t)
    };
    $(n);
    $(r)
})(window)