---
title: "Famous HNers and Their Sites"
last_modified_at: 2022-07-30
categories:
  - Blog
tags:
  - Data Analysis
---

It's been too long since I've had a little data exploration project. So I decided to track down the HN users with the most karma and explore their personal sites. More specifically, I:

1. Downloaded all HN users from BigQuery
2. Hit `"https://hacker-news.firebaseio.com/v0/user/{username}.json?print=pretty"` to get everyone's `about` and `karma` data
3. Filtered users for those with more than 10,000 karma
4. Filtered out users with empty `about` sections
5. Filtered out users with no "interesting" links. Non-interesting links include things like "twitter", "gmail", "keybase", etc. 

Past that, it was a pretty manual process. I've attempted to review everything, make sure links weren't stale, and verify that there was at least some small interesting thing on at one or more of the links. Some of these users have made it on the list from sites representing companies the user has founded. But, most of the sites are personal blogs of some sort. 

This process took me from the 807370 who have ever commented/posted on HN, to a list of 340 unique and interesting corners of the internet! 🙂

_Disclaimer:_ Despite manual spotchecking along the way, there's a chance I didn't include everyone or that some links I've included are dead. If that's the case, feel free to reach out!

## Top hits

First, here's a bonus list of sites that struck my fancy for one reason or another. They're in no particular order:

1. [https://breckyunits.com/](https://breckyunits.com/)
2. [https://corememorymusic.com/](https://corememorymusic.com/)
3. [http://egypt.urnash.com/rita/](http://egypt.urnash.com/rita/)
4. [https://www.gwern.net](https://www.gwern.net)
5. [https://edweissman.com/index.html](https://edweissman.com/index.html)
6. [https://edent.tel/](https://edent.tel/)
7. [http://www.righto.com/](http://www.righto.com/)
8. [https://jgc.org/](https://jgc.org/)
9. [https://www.sonyasupposedly.com/](https://www.sonyasupposedly.com/)
10. [https://aegir.sexy/](https://aegir.sexy/)

## Full list

### jacquesm (karma=198342)
* [https://pianojacq.com/](https://pianojacq.com/)
* [https://jacquesmattheij.com/](https://jacquesmattheij.com/)
* [https://modularcompany.com](https://modularcompany.com)
* [https://camarades.com](https://camarades.com)

### danso (karma=153582)
* [http://www.danwin.com](http://www.danwin.com)

### rbanffy (karma=128093)
* [http://about.me/rbanffy](http://about.me/rbanffy)

### patio11 (karma=127036)
* [https://www.kalzumeus.com](https://www.kalzumeus.com)

### tosh (karma=117833)
* [https://jamshelf.com](https://jamshelf.com)
* [https://magic.do](https://magic.do)
* [https://lemmings.io](https://lemmings.io)
* [https://applesilicongames.com](https://applesilicongames.com)
* [https://devmonthly.com](https://devmonthly.com)
* [https://blossom.io](https://blossom.io)
* [https://angel.co/tosh](https://angel.co/tosh)
* [https://lobste.rs/u/tosh](https://lobste.rs/u/tosh)
* [https://dribbble.com/tosh](https://dribbble.com/tosh)
* [https://instagram.com/thomas.schranz](https://instagram.com/thomas.schranz)
* [https://facebook.com/thomas.schranz](https://facebook.com/thomas.schranz)

### Animats (karma=112598)
* [https://www.animats.com](https://www.animats.com)

### TeMPOraL (karma=90749)
* [http://jacek.zlydach.pl](http://jacek.zlydach.pl)
* [http://esejepg.pl/](http://esejepg.pl/)
* [http://jacek.zlydach.pl/blog/2018-01-06-going-far-going-small.html](http://jacek.zlydach.pl/blog/2018-01-06-going-far-going-small.html)
* [https://hnbadges.netlify.app/?user=TeMPOraL](https://hnbadges.netlify.app/?user=TeMPOraL)

### luu (karma=88078)
* [https://danluu.com](https://danluu.com)

### steveklabnik (karma=84088)
* [http://steveklabnik.com](http://steveklabnik.com)

### jgrahamc (karma=82513)
* [https://jgc.org/](https://jgc.org/)

### uptown (karma=75433)
* [http://massivedesigns.com/](http://massivedesigns.com/)
* [http://dribbble.com/davidmcooper](http://dribbble.com/davidmcooper)

### jerf (karma=75058)
* [http://www.jerf.org/iri](http://www.jerf.org/iri)

### edw519 (karma=73416)
* [https://edweissman.com](https://edweissman.com)

### jseliger (karma=69872)
* [http://jakeseliger.com](http://jakeseliger.com)
* [http://www.seliger.com/blog](http://www.seliger.com/blog)

### jrockway (karma=65974)
* [https://jrock.us/](https://jrock.us/)
* [https://jrock.us/posts/](https://jrock.us/posts/)
* [https://pachyderm.com/](https://pachyderm.com/)

### tokenadult (karma=62345)
* [http://en.wikipedia.org/wiki/User:WeijiBaikeBianji/IntelligenceCitations](http://en.wikipedia.org/wiki/User:WeijiBaikeBianji/IntelligenceCitations)
* [http://en.wikipedia.org/wiki/User:WeijiBaikeBianji/AnthropologyHumanBiologyRaceCitations](http://en.wikipedia.org/wiki/User:WeijiBaikeBianji/AnthropologyHumanBiologyRaceCitations)
* [http://en.wikipedia.org/wiki/IQ_classification](http://en.wikipedia.org/wiki/IQ_classification)
* [http://learninfreedom.org/](http://learninfreedom.org/)

### aaronbrethorst (karma=60103)
* [http://www.cocoacontrols.com](http://www.cocoacontrols.com)
* [http://www.aaronbrethorstphotography.com](http://www.aaronbrethorstphotography.com)

### jedberg (karma=59475)
* [http://www.jedberg.net](http://www.jedberg.net)

### davidw (karma=58723)
* [http://www.welton.it/davidw/](http://www.welton.it/davidw/)
* [http://www.dedasys.com](http://www.dedasys.com)
* [http://davids-book-reviews.blogspot.com](http://davids-book-reviews.blogspot.com)

### cperciva (karma=58083)
* [http://www.tarsnap.com/](http://www.tarsnap.com/)

### fogus (karma=57923)
* [http://www.joyofclojure.com](http://www.joyofclojure.com)
* [http://blog.fogus.me](http://blog.fogus.me)
* [http://www.fogus.me](http://www.fogus.me)

### adamnemecek (karma=56982)
* [http://ngrid.io](http://ngrid.io)
* [http://www.syntorial.com/#a_aid=AudioKit](http://www.syntorial.com/#a_aid=AudioKit)
* [http://audiokit.io](http://audiokit.io)
* [http://www.reproducibility.org/RSF/book/bei/conj/paper_html/index.html](http://www.reproducibility.org/RSF/book/bei/conj/paper_html/index.html)

### stavros (karma=56475)
* [https://www.stavros.io](https://www.stavros.io)

### smacktoward (karma=54883)
* [https://jasonlefkowitz.net](https://jasonlefkowitz.net)

### minimaxir (karma=54543)
* [https://minimaxir.com](https://minimaxir.com)
* [https://minimaxir.com](https://minimaxir.com)
* [https://www.patreon.com/minimaxir](https://www.patreon.com/minimaxir)

### robin_reala (karma=54543)
* [https://www.robinwhittleton.com/](https://www.robinwhittleton.com/)
* [https://standardebooks.org/](https://standardebooks.org/)
* [https://www.robinwhittleton.com/books/](https://www.robinwhittleton.com/books/)

### wglb (karma=50944)
* [https://ciexinc.com](https://ciexinc.com)
* [https://ciexinc.com/](https://ciexinc.com/)

### btilly (karma=48279)
* [https://leanstreet.io/](https://leanstreet.io/)

### lisper (karma=47267)
* [http://www.rongarret.info/](http://www.rongarret.info/)

### wpietri (karma=46883)
* [http://williampietri.com/](http://williampietri.com/)
* [http://www.penny-arcade.com/comic/2004/03/19](http://www.penny-arcade.com/comic/2004/03/19)

### derefr (karma=46536)
* [https://covalenthq.com](https://covalenthq.com)

### DiabloD3 (karma=45213)
* [https://www.exelion.net/](https://www.exelion.net/)
* [http://adterrasperaspera.com/](http://adterrasperaspera.com/)

### raganwald (karma=44995)
* [http://braythwayt.com](http://braythwayt.com)

### swombat (karma=44077)
* [http://www.swombat.com](http://www.swombat.com)
* [http://danieltenner.com](http://danieltenner.com)
* [http://inter-sections.net](http://inter-sections.net)
* [http://www.granttree.co.uk](http://www.granttree.co.uk)
* [http://blog.granttree.co.uk](http://blog.granttree.co.uk)

### mooreds (karma=43991)
* [https://fusionauth.io/](https://fusionauth.io/)
* [https://fusionauth.io/jobs/](https://fusionauth.io/jobs/)
* [https://www.mooreds.com](https://www.mooreds.com)
* [https://letterstoanewdeveloper.com/](https://letterstoanewdeveloper.com/)
* [https://hnbadges.netlify.app/?user=mooreds](https://hnbadges.netlify.app/?user=mooreds)

### DanielBMarkham (karma=43827)
* [https://discord.gg/fR8dG5XePM](https://discord.gg/fR8dG5XePM)
* [http://bedfordtechnologygroup.com/links.html](http://bedfordtechnologygroup.com/links.html)

### bpierre (karma=43169)
* [https://bpier.re/](https://bpier.re/)

### Anon84 (karma=43072)
* [https://graphs4sci.substack.com](https://graphs4sci.substack.com)
* [https://viz4sci.substack.com](https://viz4sci.substack.com)
* [https://www.data4sci.com/newsletter](https://www.data4sci.com/newsletter)
* [https://www.bgoncalves.com/](https://www.bgoncalves.com/)

### doener (karma=42651)
* [https://www.fph.berlin](https://www.fph.berlin)

### mpweiher (karma=42626)
* [http://blog.metaobject.com/](http://blog.metaobject.com/)
* [http://www.metaobject.com/](http://www.metaobject.com/)
* [http://objective.st/](http://objective.st/)

### yummyfajitas (karma=41933)
* [http://www.chrisstucchio.com](http://www.chrisstucchio.com)

### bookofjoe (karma=41555)
* [https://scholar.google.com/citations?user=5DdrMc8AAAAJ&hl=en](https://scholar.google.com/citations?user=5DdrMc8AAAAJ&hl=en)
* [https://www.bookofjoe.com/](https://www.bookofjoe.com/)
* [https://everything.typepad.com/blog/2017/07/interview-with-joe-from-the-bookofjoe-blog.html](https://everything.typepad.com/blog/2017/07/interview-with-joe-from-the-bookofjoe-blog.html)
* [https://www.amazon.com/s?](https://www.amazon.com/s?)

### JoshTriplett (karma=40029)
* [https://joshtriplett.org](https://joshtriplett.org)

### DoreenMichele (karma=39415)
* [https://projectsro.blogspot.com/](https://projectsro.blogspot.com/)
* [https://Eclogiselle.com](https://Eclogiselle.com)

### onion2k (karma=39102)
* [http://ooer.com](http://ooer.com)

### sethbannon (karma=37954)
* [http://fiftyyears.com/](http://fiftyyears.com/)
* [http://impact.tech/](http://impact.tech/)
* [http://sethbannon.com](http://sethbannon.com)

### grellas (karma=37827)
* [http://www.grellas.com](http://www.grellas.com)
* [https://grellas.com/resources/startup-101/](https://grellas.com/resources/startup-101/)

### feross (karma=36496)
* [https://feross.org/resume](https://feross.org/resume)

### brundolf (karma=35905)
* [https://www.brandons.me/](https://www.brandons.me/)

### munificent (karma=34358)
* [https://gameprogrammingpatterns.com](https://gameprogrammingpatterns.com)

### benbreen (karma=33963)
* [https://benjaminpbreen.com](https://benjaminpbreen.com)

### vidarh (karma=33832)
* [https://accelerated.ventures/](https://accelerated.ventures/)
* [http://www.hokstad.com](http://www.hokstad.com)
* [http://www.hokstad.com/blog](http://www.hokstad.com/blog)
* [https://galaxybound.com](https://galaxybound.com)
* [http://www.hokstad.com/compiler](http://www.hokstad.com/compiler)

### scott_s (karma=33788)
* [http://www.scott-a-s.com](http://www.scott-a-s.com)

### lmm (karma=33496)
* [https://m50d.github.io/](https://m50d.github.io/)

### SwellJoe (karma=32707)
* [http://www.virtualmin.com](http://www.virtualmin.com)
* [http://swelljoe.com](http://swelljoe.com)

### mindcrime (karma=32272)
* [http://www.quora.com/Phillip-Rhodes](http://www.quora.com/Phillip-Rhodes)
* [http://www.fogbeam.com](http://www.fogbeam.com)

### barrkel (karma=31918)
* [http://blog.barrkel.com/](http://blog.barrkel.com/)

### mhb (karma=31666)
* [https://www.bermita.com](https://www.bermita.com)

### gwern (karma=30408)
* [https://www.gwern.net](https://www.gwern.net)
* [https://www.gwern.net/Links](https://www.gwern.net/Links)
* [https://www.gwern.net/Changelog](https://www.gwern.net/Changelog)
* [https://www.gwern.net/Links#contact](https://www.gwern.net/Links#contact)

### tlrobinson (karma=30217)
* [http://tlrobinson.net](http://tlrobinson.net)
* [http://www.metabase.com/](http://www.metabase.com/)
* [http://www.crunchbase.com/company/280-north](http://www.crunchbase.com/company/280-north)
* [http://www.cappuccino-project.org/](http://www.cappuccino-project.org/)

### apsec112 (karma=30158)
* [http://www.rationalconspiracy.com/](http://www.rationalconspiracy.com/)

### pavlov (karma=29939)
* [https://reactstudio.com](https://reactstudio.com)
* [https://app.rodeo](https://app.rodeo)

### craigkerstiens (karma=29560)
* [https://www.crunchydata.com](https://www.crunchydata.com)
* [https://www.crunchybridge.com](https://www.crunchybridge.com)
* [https://www.craigkerstiens.com](https://www.craigkerstiens.com)

### Alex3917 (karma=29455)
* [https://www.fwdeveryone.com](https://www.fwdeveryone.com)
* [https://alexkrupp.typepad.com](https://alexkrupp.typepad.com)

### geofft (karma=29347)
* [https://ldpreload.com/](https://ldpreload.com/)
* [https://looseleafsecurity.com](https://looseleafsecurity.com)

### giuliomagnifico (karma=29156)
* [https://giuliomagnifico.blog](https://giuliomagnifico.blog)
* [https://giuliomagnifico.it](https://giuliomagnifico.it)

### fanf2 (karma=29087)
* [https://dotat.at](https://dotat.at)
* [https://fanf.dreamwidth.org](https://fanf.dreamwidth.org)
* [https://isc.org](https://isc.org)

### sinak (karma=28589)
* [https://Repair.org](https://Repair.org)

### gojomo (karma=28509)
* [http://thunkpedia.org](http://thunkpedia.org)
* [http://memesteading.com](http://memesteading.com)
* [http://gojomo.blogspot.com](http://gojomo.blogspot.com)
* [http://xavvy.com](http://xavvy.com)

### PaulHoule (karma=27729)
* [http://ontology2.com/o/help.html](http://ontology2.com/o/help.html)

### denzil_correa (karma=27567)
* [http://correa.in](http://correa.in)

### skrebbel (karma=27432)
* [https://talkjs.com](https://talkjs.com)

### eli (karma=27248)
* [https://industrydive.com](https://industrydive.com)
* [https://www.utilitydive.com/](https://www.utilitydive.com/)
* [https://www.biopharmadive.com/](https://www.biopharmadive.com/)
* [https://www.supplychaindive.com/](https://www.supplychaindive.com/)
* [https://www.industrydive.com/industries/](https://www.industrydive.com/industries/)
* [https://eli.at.industrydive.com](https://eli.at.industrydive.com)
* [http://www.elidickinson.com/](http://www.elidickinson.com/)

### adrianN (karma=27082)
* [http://adriann.github.io](http://adriann.github.io)

### scrollaway (karma=26799)
* [https://leclan.ch](https://leclan.ch)

### joeyespo (karma=26511)
* [https://joeyespo.com](https://joeyespo.com)

### _pius (karma=26408)
* [https://pius.me](https://pius.me)

### simonw (karma=26388)
* [https://simonwillison.net/](https://simonwillison.net/)

### api (karma=25877)
* [http://adamierymenko.com/](http://adamierymenko.com/)
* [https://www.zerotier.com/](https://www.zerotier.com/)

### pcr910303 (karma=25610)
* [https://daum.net](https://daum.net)

### rwmj (karma=25505)
* [https://rwmj.wordpress.com/](https://rwmj.wordpress.com/)

### ddevault (karma=25484)
* [https://drewdevault.com](https://drewdevault.com)

### djsumdog (karma=25430)
* [https://battlepenguin.com](https://battlepenguin.com)

### ComputerGuru (karma=25219)
* [http://neosmart.net/](http://neosmart.net/)
* [https://neosmart.net/downloads/miscellania/mqudsi.asc](https://neosmart.net/downloads/miscellania/mqudsi.asc)

### wslh (karma=24713)
* [https://www.natural.do/](https://www.natural.do/)
* [https://www.coinfabrik.com](https://www.coinfabrik.com)
* [https://www.nektra.com](https://www.nektra.com)
* [https://blog.coinfabrik.com](https://blog.coinfabrik.com)
* [https://blog.nektra.com](https://blog.nektra.com)
* [https://blog.databigbang.com](https://blog.databigbang.com)

### manigandham (karma=24619)
* [https://manigandham.com](https://manigandham.com)

### dasil003 (karma=24556)
* [https://mubi.com/users/2](https://mubi.com/users/2)
* [http://websaviour.com/](http://websaviour.com/)

### modeless (karma=24489)
* [https://james.darpinian.com/satellites/](https://james.darpinian.com/satellites/)

### acdha (karma=24467)
* [https://chris.improbable.org](https://chris.improbable.org)

### duck (karma=24171)
* [http://www.hackernewsletter.com](http://www.hackernewsletter.com)
* [http://www.kaledavis.com](http://www.kaledavis.com)

### jsnell (karma=24167)
* [https://www.snellman.net/](https://www.snellman.net/)

### pabs3 (karma=24162)
* [https://bonedaddy.net/pabs3/](https://bonedaddy.net/pabs3/)
* [https://bonedaddy.net/pabs3/about/resume/](https://bonedaddy.net/pabs3/about/resume/)
* [https://bonedaddy.net/pabs3/about/#other_pages](https://bonedaddy.net/pabs3/about/#other_pages)
* [https://bonedaddy.net/pabs3/log/](https://bonedaddy.net/pabs3/log/)
* [https://bonedaddy.net/pabs3/about/#contact](https://bonedaddy.net/pabs3/about/#contact)

### idlewords (karma=23398)
* [http://idlewords.com](http://idlewords.com)
* [http://pinboard.in](http://pinboard.in)
* [http://bedbugregistry.com](http://bedbugregistry.com)

### ocdtrekkie (karma=23378)
* [https://ocdtrekkie.com](https://ocdtrekkie.com)

### antirez (karma=23093)
* [http://invece.org](http://invece.org)
* [http://antirez.com](http://antirez.com)

### ph0rque (karma=23071)
* [https://AutoMicroFarm.com](https://AutoMicroFarm.com)

### kazinator (karma=23022)
* [http://nongnu.org/txr](http://nongnu.org/txr)

### simonebrunozzi (karma=22761)
* [http://brunozzi.com/](http://brunozzi.com/)

### kf (karma=22755)
* [https://www.getkratom.com](https://www.getkratom.com)

### rms (karma=22600)
* [http://www.cryptolotus.com](http://www.cryptolotus.com)

### dangrossman (karma=22331)
* [http://www.hnreplies.com](http://www.hnreplies.com)
* [https://improvely.com](https://improvely.com)
* [https://w3counter.com](https://w3counter.com)
* [https://ligninandlight.com](https://ligninandlight.com)
* [https://glowforge.us/r/GMSCZQGJ](https://glowforge.us/r/GMSCZQGJ)

### jasonkester (karma=22264)
* [http://www.expatsoftware.com/](http://www.expatsoftware.com/)
* [http://www.expatsoftware.com/articles](http://www.expatsoftware.com/articles)
* [https://unwaffle.com/](https://unwaffle.com/)
* [http://www.twiddla.com/](http://www.twiddla.com/)
* [https://www.s3stat.com/](https://www.s3stat.com/)

### austenallred (karma=22228)
* [https://bloomtech.com](https://bloomtech.com)

### jasonlbaptiste (karma=22126)
* [http://www.jasonlbaptiste.com](http://www.jasonlbaptiste.com)

### kragen (karma=22074)
* [http://canonical.org/~kragen/](http://canonical.org/~kragen/)

### gkoberger (karma=22069)
* [http://readme.com](http://readme.com)
* [http://readme.com/careers](http://readme.com/careers)

### gk1 (karma=21774)
* [https://www.pinecone.io](https://www.pinecone.io)
* [https://www.gkogan.co](https://www.gkogan.co)
* [https://www.gregkogan.com](https://www.gregkogan.com)

### michaelt (karma=21520)
* [http://www.mjt.me.uk](http://www.mjt.me.uk)

### simonsarris (karma=21500)
* [https://simonsarris.substack.com](https://simonsarris.substack.com)
* [http://gojs.net/](http://gojs.net/)

### mbrubeck (karma=21171)
* [http://limpet.net/mbrubeck/](http://limpet.net/mbrubeck/)

### Brajeshwar (karma=21128)
* [https://brajeshwar.com](https://brajeshwar.com)
* [https://valinor.earth](https://valinor.earth)

### buro9 (karma=20660)
* [https://grafana.com/about/careers/#jobs](https://grafana.com/about/careers/#jobs)
* [https://www.lfgss.com/](https://www.lfgss.com/)
* [https://david.kitchen](https://david.kitchen)

### edent (karma=20504)
* [https://shkspr.mobi/blog/](https://shkspr.mobi/blog/)
* [https://edent.tel/](https://edent.tel/)

### imartin2k (karma=20412)
* [http://swedishtechweekly.com](http://swedishtechweekly.com)

### pron (karma=20389)
* [https://pron.github.io/](https://pron.github.io/)

### CPLX (karma=20359)
* [https://fromdayone.co](https://fromdayone.co)

### dsr_ (karma=20267)
* [https://blog.randomstring.org](https://blog.randomstring.org)

### chmaynard (karma=20195)
* [https://corememorymusic.com](https://corememorymusic.com)

### iamelgringo (karma=20102)
* [http://www.hackersandfounders.com](http://www.hackersandfounders.com)
* [http://angel.co/hackers_and_founders](http://angel.co/hackers_and_founders)

### ryanwaggoner (karma=20078)
* [https://ryanwaggoner.com](https://ryanwaggoner.com)

### acangiano (karma=19981)
* [https://antoniocangiano.com](https://antoniocangiano.com)
* [https://pragprog.com/book/actb2/technical-blogging-second-edition](https://pragprog.com/book/actb2/technical-blogging-second-edition)

### grey-area (karma=19960)
* [https://bedful.com](https://bedful.com)
* [https://projectpage.app](https://projectpage.app)
* [https://golangnews.com](https://golangnews.com)

### revorad (karma=19938)
* [https://Learnetto.com](https://Learnetto.com)

### mrb (karma=19905)
* [http://zorinaq.com](http://zorinaq.com)
* [http://blog.zorinaq.com](http://blog.zorinaq.com)

### Sir_Cmpwn (karma=19702)
* [https://drewdevault.com](https://drewdevault.com)

### nailer (karma=19702)
* [https://mikemaccana.com](https://mikemaccana.com)

### wlesieutre (karma=19699)
* [https://will.institute](https://will.institute)

### nine_k (karma=19681)
* [http://dmitry.cheryasov.info/resume.html](http://dmitry.cheryasov.info/resume.html)

### grecy (karma=19678)
* [http://theroadchoseme.com](http://theroadchoseme.com)
* [http://wikioverland.org](http://wikioverland.org)

### sneak (karma=19582)
* [https://sneak.berlin/](https://sneak.berlin/)
* [https://bbs.sneak.berlin](https://bbs.sneak.berlin)

### chimeracoder (karma=19349)
* [http://www.adityamukerjee.net/](http://www.adityamukerjee.net/)

### mortenjorck (karma=19283)
* [https://interuserface.net](https://interuserface.net)

### leephillips (karma=19229)
* [https://lee-phillips.org](https://lee-phillips.org)
* [https://CVservant.com](https://CVservant.com)
* [https://picmunge.cvservant.com](https://picmunge.cvservant.com)
* [https://goo.gl/HrS8sV](https://goo.gl/HrS8sV)
* [https://alogus.com/publishing/gnuplot5/](https://alogus.com/publishing/gnuplot5/)

### imgabe (karma=19094)
* [https://tiltingatwindmills.dev](https://tiltingatwindmills.dev)
* [https://kotsf.com](https://kotsf.com)
* [https://nononsense.recipes](https://nononsense.recipes)

### vinnyglennon (karma=19088)
* [https://hnify.com](https://hnify.com)
* [https://WebSummit.com](https://WebSummit.com)
* [https://FanFootage.com](https://FanFootage.com)
* [https://SeenBefore.com](https://SeenBefore.com)
* [https://FantasyTote.com](https://FantasyTote.com)

### jessriedel (karma=18982)
* [https://jessriedel.com](https://jessriedel.com)

### paulgb (karma=18891)
* [https://driftingin.space](https://driftingin.space)
* [https://paulbutler.org](https://paulbutler.org)

### danShumway (karma=18882)
* [https://danshumway.com](https://danshumway.com)

### prawn (karma=18690)
* [http://isaacforman.com.au](http://isaacforman.com.au)
* [https://usepunch.com/](https://usepunch.com/)
* [https://serio.com.au/](https://serio.com.au/)
* [https://beamorders.com/](https://beamorders.com/)
* [http://hexiledgame.com/](http://hexiledgame.com/)
* [http://streaksapp.com/](http://streaksapp.com/)
* [http://streaksworkout.com/](http://streaksworkout.com/)
* [https://vanspiration.com/](https://vanspiration.com/)
* [http://www.313halifax.com.au/](http://www.313halifax.com.au/)
* [http://shubbo.com/](http://shubbo.com/)

### ISL (karma=18516)
* [http://charliehagedorn.com](http://charliehagedorn.com)
* [http://nanoradian.com](http://nanoradian.com)
* [http://measuredmass.com](http://measuredmass.com)
* [https://www.instagram.com/charliehagedorn/](https://www.instagram.com/charliehagedorn/)

### marcosdumay (karma=18448)
* [https://marcosdumay.com](https://marcosdumay.com)
* [https://sealgram.com](https://sealgram.com)
* [http://marcosdumay.com/rapid-django](http://marcosdumay.com/rapid-django)

### mixmax (karma=18148)
* [http://www.maximise.dk](http://www.maximise.dk)

### IgorPartola (karma=18012)
* [http://igorpartola.com](http://igorpartola.com)
* [http://family-fortune.ridgebit.com/](http://family-fortune.ridgebit.com/)
* [https://igorpartola.com](https://igorpartola.com)

### timf (karma=17985)
* [https://www.peakscale.com/about/](https://www.peakscale.com/about/)

### jamesjyu (karma=17933)
* [https://www.jamesyu.org](https://www.jamesyu.org)

### wheels (karma=17913)
* [http://www.directededge.com/](http://www.directededge.com/)
* [http://scotchi.net/](http://scotchi.net/)

### dnautics (karma=17904)
* [http://www.rexcomputing.com/](http://www.rexcomputing.com/)

### kalleboo (karma=17903)
* [http://www.kalleboo.com/retrotech/](http://www.kalleboo.com/retrotech/)

### fossuser (karma=17619)
* [https://zalberico.com/](https://zalberico.com/)
* [https://zalberico.com/about/](https://zalberico.com/about/)
* [https://old.reddit.com/r/hnblogs/](https://old.reddit.com/r/hnblogs/)

### nikcub (karma=17566)
* [https://nikcub.me](https://nikcub.me)

### schoen (karma=17522)
* [https://jhalderm.com/pub/papers/letsencrypt-ccs19.pdf](https://jhalderm.com/pub/papers/letsencrypt-ccs19.pdf)
* [https://jhalderm.com/pub/papers/coldboot-sec08.pdf](https://jhalderm.com/pub/papers/coldboot-sec08.pdf)
* [https://sethschoen.com/](https://sethschoen.com/)

### JonnieCache (karma=17245)
* [http://unmode.com](http://unmode.com)

### tysone (karma=17235)
* [http://tysonevans.com](http://tysonevans.com)

### londons_explore (karma=17184)
* [https://omattos.com/contact](https://omattos.com/contact)

### bensummers (karma=16964)
* [http://bens.me.uk](http://bens.me.uk)
* [http://haplo.org](http://haplo.org)
* [http://www.haplo-services.com/jobs](http://www.haplo-services.com/jobs)

### matthewmacleod (karma=16954)
* [https://matt-m.co.uk](https://matt-m.co.uk)
* [https://botsandus.com](https://botsandus.com)

### woodruffw (karma=16897)
* [https://yossarian.net](https://yossarian.net)
* [https://blog.yossarian.net](https://blog.yossarian.net)

### RyanMcGreal (karma=16891)
* [http://quandyfactory.com](http://quandyfactory.com)

### Symmetry (karma=16876)
* [http://www.righthandrobotics.com/](http://www.righthandrobotics.com/)
* [http://hopefullyintersting.blogspot.com/](http://hopefullyintersting.blogspot.com/)

### mcguire (karma=16841)
* [http://maniagnosis.crsr.net](http://maniagnosis.crsr.net)

### kstenerud (karma=16833)
* [https://concise-encoding.org/](https://concise-encoding.org/)

### willvarfar (karma=16774)
* [http://williamedwardscoder.tumblr.com/](http://williamedwardscoder.tumblr.com/)

### abraham (karma=16713)
* [https://abrah.am/](https://abrah.am/)

### jstanley (karma=16694)
* [https://incoherency.co.uk/](https://incoherency.co.uk/)

### pc (karma=16676)
* [http://patrickcollison.com](http://patrickcollison.com)

### SilasX (karma=16646)
* [http://blog.tyrannyofthemouse.com](http://blog.tyrannyofthemouse.com)

### ca98am79 (karma=16622)
* [https://wizehive.com](https://wizehive.com)

### Vinnl (karma=16620)
* [https://solidproject.org](https://solidproject.org)
* [https://plaudit.pub](https://plaudit.pub)
* [https://vincenttunru.com](https://vincenttunru.com)

### stickfigure (karma=16610)
* [https://www.orbitkit.com/](https://www.orbitkit.com/)
* [http://www.motomapia.com/](http://www.motomapia.com/)
* [http://mav.sourceforge.net/](http://mav.sourceforge.net/)
* [https://www.gearlaunch.com/](https://www.gearlaunch.com/)
* [https://www.voo.st/](https://www.voo.st/)
* [http://www.similarity.com/](http://www.similarity.com/)
* [http://www.mobca.st/](http://www.mobca.st/)
* [http://www.advrider.com/forums/showthread.php?t=457038](http://www.advrider.com/forums/showthread.php?t=457038)
* [http://www.advrider.com/forums/showthread.php?t=305107](http://www.advrider.com/forums/showthread.php?t=305107)

### Lazare (karma=16544)
* [https://mobihq.com/](https://mobihq.com/)

### ot (karma=16461)
* [http://www.di.unipi.it/~ottavian/](http://www.di.unipi.it/~ottavian/)

### daenz (karma=16426)
* [https://www.arwmoffat.com/](https://www.arwmoffat.com/)

### weinzierl (karma=16410)
* [https://weinzierlweb.com](https://weinzierlweb.com)

### mark_l_watson (karma=16352)
* [https://markwatson.com](https://markwatson.com)
* [https://leanpub.com/u/markwatson](https://leanpub.com/u/markwatson)

### bambax (karma=16297)
* [https://www.babeloop.com](https://www.babeloop.com)
* [https://open.spotify.com/artist/5WHf35J0rrVKA8a20ANZUp](https://open.spotify.com/artist/5WHf35J0rrVKA8a20ANZUp)

### danilocampos (karma=16274)
* [http://danilocampos.com](http://danilocampos.com)

### echelon (karma=16234)
* [https://fakeyou.com](https://fakeyou.com)
* [https://storyteller.io](https://storyteller.io)

### umvi (karma=16136)
* [https://www.bryanpg.com/](https://www.bryanpg.com/)

### Karunamon (karma=16135)
* [http://tkware.info](http://tkware.info)

### sciurus (karma=16097)
* [https://www.polibyte.com](https://www.polibyte.com)

### chrismorgan (karma=16078)
* [https://chrismorgan.info/](https://chrismorgan.info/)
* [https://chrismorgan.info/hire-me/](https://chrismorgan.info/hire-me/)

### atombender (karma=16005)
* [https://sanity.io/](https://sanity.io/)

### dwynings (karma=15986)
* [http://druwynings.com](http://druwynings.com)
* [http://www.diffbot.com/](http://www.diffbot.com/)

### Pxtl (karma=15958)
* [https://www.pxtl.ca/](https://www.pxtl.ca/)

### geerlingguy (karma=15915)
* [https://www.jeffgeerling.com/](https://www.jeffgeerling.com/)

### sant0sk1 (karma=15877)
* [http://jerodsanto.net](http://jerodsanto.net)
* [http://blog.jerodsanto.net](http://blog.jerodsanto.net)

### joshuacc (karma=15840)
* [http://designpepper.com/a-drip-of-javascript](http://designpepper.com/a-drip-of-javascript)
* [http://joshuaclanton.dev](http://joshuaclanton.dev)
* [http://myhnstory.com/joshuacc/](http://myhnstory.com/joshuacc/)

### andybak (karma=15703)
* [http://www.ixxy.co.uk/](http://www.ixxy.co.uk/)
* [http://www.andybak.net](http://www.andybak.net)
* [https://linktr.ee/andybak](https://linktr.ee/andybak)

### ChrisMarshallNY (karma=15645)
* [https://riftvalleysoftware.com](https://riftvalleysoftware.com)
* [https://littlegreenviper.com](https://littlegreenviper.com)

### rmc (karma=15638)
* [http://www.celtic-knot-creator.com](http://www.celtic-knot-creator.com)
* [http://www.kindle-maps.com](http://www.kindle-maps.com)

### azhenley (karma=15557)
* [http://austinhenley.com](http://austinhenley.com)

### _0nac (karma=15551)
* [http://gyrovague.com](http://gyrovague.com)

### graeme (karma=15543)
* [https://lsathacks.com](https://lsathacks.com)
* [http://lsathacks.com](http://lsathacks.com)

### jpatokal (karma=15525)
* [http://gyrovague.com](http://gyrovague.com)

### nullc (karma=15514)
* [http://nt4tn.net/](http://nt4tn.net/)

### paul (karma=15468)
* [http://paulbuchheit.blogspot.com/](http://paulbuchheit.blogspot.com/)
* [http://en.wikipedia.org/wiki/Paul_Buchheit](http://en.wikipedia.org/wiki/Paul_Buchheit)

### jeffbarr (karma=15365)
* [http://aws.amazon.com/blogs/aws/](http://aws.amazon.com/blogs/aws/)
* [http://www.jeff-barr.com](http://www.jeff-barr.com)
* [http://aws.amazon.com](http://aws.amazon.com)

### jefftk (karma=15355)
* [https://www.jefftk.com](https://www.jefftk.com)
* [https://www.jefftk.com/p/leaving-google-joining-the-nucleic-acid-observatory](https://www.jefftk.com/p/leaving-google-joining-the-nucleic-acid-observatory)

### awb (karma=15302)
* [https://www.andybrewer.com](https://www.andybrewer.com)

### ryan_j_naughton (karma=15269)
* [https://newdata.org](https://newdata.org)
* [https://Fair.com](https://Fair.com)

### jwr (karma=15268)
* [https://partsbox.com/](https://partsbox.com/)
* [https://jan.rychter.com/0x49248F8CF128664B.txt](https://jan.rychter.com/0x49248F8CF128664B.txt)

### throwanem (karma=15242)
* [https://aaron-m.com](https://aaron-m.com)

### cstross (karma=15125)
* [https://www.accelerando.org/](https://www.accelerando.org/)

### arkadiyt (karma=15100)
* [https://arkadiyt.com/about](https://arkadiyt.com/about)

### coffeemug (karma=15035)
* [http://www.rethinkdb.com](http://www.rethinkdb.com)
* [http://www.defmacro.org](http://www.defmacro.org)

### mgkimsal (karma=15015)
* [https://kimsal.com](https://kimsal.com)

### pornel (karma=14938)
* [https://kornel.ski](https://kornel.ski)

### AndrewKemendo (karma=14893)
* [https://kemendo.com](https://kemendo.com)
* [https://findcovidtesting.com](https://findcovidtesting.com)

### p4bl0 (karma=14862)
* [https://pablo.rauzy.name/](https://pablo.rauzy.name/)
* [http://c2fk5i7jqn7am7nfo7eb7hwrkclyj3jj4qcwgdh6ievp7v5ie4gd3mid.onion/](http://c2fk5i7jqn7am7nfo7eb7hwrkclyj3jj4qcwgdh6ievp7v5ie4gd3mid.onion/)

### dvt (karma=14829)
* [https://dvt.name](https://dvt.name)

### Sami_Lehtinen (karma=14816)
* [https://www.sami-lehtinen.net](https://www.sami-lehtinen.net)

### ThomPete (karma=14807)
* [https://www.firstprinciple.co](https://www.firstprinciple.co)
* [https://www.hellogroup.com](https://www.hellogroup.com)
* [https://www.thenorthalliance.com/](https://www.thenorthalliance.com/)
* [https://www.Ghostnoteapp.com](https://www.Ghostnoteapp.com)
* [http://www.000fff.org](http://www.000fff.org)
* [http://mashable.com/2012/04/19/pinview-facebook-pinterest-app/](http://mashable.com/2012/04/19/pinview-facebook-pinterest-app/)

### lucb1e (karma=14763)
* [https://lucb1e.com/email-address](https://lucb1e.com/email-address)

### rossdavidh (karma=14751)
* [https://www.rosshartshorn.net](https://www.rosshartshorn.net)

### josteink (karma=14536)
* [https://jostein.kjonigsen.net](https://jostein.kjonigsen.net)

### driverdan (karma=14520)
* [http://driverdan.com](http://driverdan.com)

### ErrantX (karma=14474)
* [http://www.errant.me.uk/](http://www.errant.me.uk/)
* [http://www.errant.me.uk/blog/2009/10/pro-tip-tell-us-exactly-what-your-offering/](http://www.errant.me.uk/blog/2009/10/pro-tip-tell-us-exactly-what-your-offering/)

### dgellow (karma=14400)
* [https://sam.elborai.me](https://sam.elborai.me)

### majewsky (karma=14390)
* [https://xyrillian.de](https://xyrillian.de)

### sarchertech (karma=14379)
* [https://www.networksfromscratch.com](https://www.networksfromscratch.com)

### komali2 (karma=14351)
* [https://blog.calebjay.com](https://blog.calebjay.com)

### gscott (karma=14229)
* [https://www.easytrafficschool.com](https://www.easytrafficschool.com)
* [https://www.losangelestrafficschool.com](https://www.losangelestrafficschool.com)

### rcarmo (karma=14224)
* [https://carmo.io](https://carmo.io)
* [https://taoofmac.com](https://taoofmac.com)

### lkrubner (karma=14202)
* [https://www.amazon.com/dp/B09SFRNJKS/](https://www.amazon.com/dp/B09SFRNJKS/)
* [https://www.amazon.com/Destroy-Tech-Startup-Easy-Steps/dp/0998997617/](https://www.amazon.com/Destroy-Tech-Startup-Easy-Steps/dp/0998997617/)
* [https://demodexio.substack.com](https://demodexio.substack.com)

### orf (karma=14194)
* [https://tomforb.es](https://tomforb.es)

### pilif (karma=14187)
* [http://pilif.me](http://pilif.me)

### georgemcbay (karma=14186)
* [http://gmcbay.com](http://gmcbay.com)

### kens (karma=14131)
* [http://righto.com](http://righto.com)

### riffraff (karma=14126)
* [http://www.riffraff.info](http://www.riffraff.info)

### mmaunder (karma=14109)
* [https://www.wordfence.com/](https://www.wordfence.com/)
* [https://www.defiant.com/](https://www.defiant.com/)

### jbk (karma=13998)
* [https://videolan.org](https://videolan.org)
* [http://www.jbkempf.com/](http://www.jbkempf.com/)
* [http://www.ohloh.net/accounts/jbkempf](http://www.ohloh.net/accounts/jbkempf)

### erikpukinskis (karma=13930)
* [http://sproutrobot.com](http://sproutrobot.com)
* [http://snowedin.net](http://snowedin.net)

### coldpie (karma=13916)
* [https://smokingonabike.com](https://smokingonabike.com)

### vorpalhex (karma=13877)
* [https://vorpalhex.com](https://vorpalhex.com)

### sillysaurusx (karma=13842)
* [https://status.shawwn.com](https://status.shawwn.com)

### breck (karma=13793)
* [https://scroll.pub](https://scroll.pub)
* [https://breckyunits.com/](https://breckyunits.com/)
* [https://ourworldindata.org/](https://ourworldindata.org/)
* [https://www.uhcancercenter.org/](https://www.uhcancercenter.org/)
* [http://microsoft.com/](http://microsoft.com/)
* [https://breckyunits.com/#nudgepad-an-ide-in-your-browser](https://breckyunits.com/#nudgepad-an-ide-in-your-browser)
* [https://www.mozillalabs.com/webfwd/](https://www.mozillalabs.com/webfwd/)
* [http://labzero.com/](http://labzero.com/)
* [http://duke.edu/](http://duke.edu/)

### hannob (karma=13775)
* [https://hboeck.de/](https://hboeck.de/)

### franze (karma=13671)
* [http://f19n.com/](http://f19n.com/)
* [http://www.viennajs.org/](http://www.viennajs.org/)
* [https://www.fullstackoptimization.com/b/understanding-seo](https://www.fullstackoptimization.com/b/understanding-seo)
* [https://chrome.google.com/webstore/detail/f19n-obtrusive-live-test/jbnaibigcohjfefpfocphcjeliohhold](https://chrome.google.com/webstore/detail/f19n-obtrusive-live-test/jbnaibigcohjfefpfocphcjeliohhold)

### tikhonj (karma=13665)
* [http://jelv.is](http://jelv.is)

### andreyf (karma=13660)
* [http://anfedorov.com/](http://anfedorov.com/)

### janvdberg (karma=13547)
* [https://j11g.com](https://j11g.com)
* [https://hnbadges.netlify.app/?user=janvdberg](https://hnbadges.netlify.app/?user=janvdberg)

### mikecane (karma=13512)
* [http://mikecanex.wordpress.com](http://mikecanex.wordpress.com)

### tonyedgecombe (karma=13503)
* [https://www.tonyedgecombe.com](https://www.tonyedgecombe.com)
* [https://www.printdistributor.com](https://www.printdistributor.com)

### sebg (karma=13493)
* [https://www.datascienceweekly.org](https://www.datascienceweekly.org)
* [https://www.aiworkbox.com](https://www.aiworkbox.com)
* [https://www.dashingd3js.com](https://www.dashingd3js.com)

### dchest (karma=13394)
* [http://iwl.me](http://iwl.me)
* [https://dchest.com/authbook/](https://dchest.com/authbook/)
* [https://dchest.com](https://dchest.com)

### samatman (karma=13391)
* [http://mnemnion.github.io](http://mnemnion.github.io)

### dankohn1 (karma=13382)
* [https://www.dankohn.com](https://www.dankohn.com)
* [https://dankohn.com](https://dankohn.com)
* [https://linuxfoundation.org](https://linuxfoundation.org)

### latch (karma=13203)
* [https://www.openmymind.net](https://www.openmymind.net)

### jawns (karma=13099)
* [http://www.experimentingwithbabies.com](http://www.experimentingwithbabies.com)
* [http://www.correlated.org](http://www.correlated.org)
* [https://newlywed.science](https://newlywed.science)
* [http://www.experimentingwithbabies.com/kids](http://www.experimentingwithbabies.com/kids)
* [https://shaungallagher.pressbin.com](https://shaungallagher.pressbin.com)

### ignoramous (karma=13070)
* [https://rethinkdns.com/](https://rethinkdns.com/)

### carbocation (karma=13035)
* [https://carbocation.com](https://carbocation.com)

### danieltillett (karma=13028)
* [https://www.nucleics.com](https://www.nucleics.com)
* [https://www.tillett.info](https://www.tillett.info)

### ivankirigin (karma=12976)
* [https://write.kirigin.com](https://write.kirigin.com)
* [http://www.facebook.com/ikirigin](http://www.facebook.com/ikirigin)

### mike-cardwell (karma=12969)
* [https://www.hardenize.com/](https://www.hardenize.com/)
* [https://www.grepular.com/blog/](https://www.grepular.com/blog/)
* [https://gitlab.com/mikecardwell](https://gitlab.com/mikecardwell)
* [https://mike.cardwell([-at-])grepular.com](https://mike.cardwell([-at-])grepular.com)
* [https//www.grepular.com/1801A332.txt](https//www.grepular.com/1801A332.txt)
* [https://www.paypal.me/grepular](https://www.paypal.me/grepular)

### iamwil (karma=12939)
* [https://pulley.com](https://pulley.com)
* [https://dirtprotocol.com](https://dirtprotocol.com)
* [https://helmspoint.com](https://helmspoint.com)
* [https://www.pebble.com](https://www.pebble.com)
* [https://cubehero.com](https://cubehero.com)
* [http://noteleaf.com](http://noteleaf.com)
* [https://techcrunch.com/2008/10/23/frogmetrics-handheld-surveys-you-might-actually-want-to-fill-out/](https://techcrunch.com/2008/10/23/frogmetrics-handheld-surveys-you-might-actually-want-to-fill-out/)
* [https://isitrecession.com](https://isitrecession.com)

### dctoedt (karma=12819)
* [http://www.OnContracts.com/notebook](http://www.OnContracts.com/notebook)
* [http://www.OnContracts.com/startup-law](http://www.OnContracts.com/startup-law)
* [http://www.QuestioningChristian.org](http://www.QuestioningChristian.org)
* [http://www.OnContracts.com/About](http://www.OnContracts.com/About)

### JshWright (karma=12804)
* [https://elationhealth.com](https://elationhealth.com)

### kjhughes (karma=12726)
* [http://www.entel.com](http://www.entel.com)

### k__ (karma=12725)
* [https://kay.is](https://kay.is)
* [https://fllstck.dev](https://fllstck.dev)
* [https://www.newline.co/react-from-zero/](https://www.newline.co/react-from-zero/)
* [https://blog.developerdao.com](https://blog.developerdao.com)

### Symbiote (karma=12687)
* [https://aposymbiont.github.io/split-keyboards/](https://aposymbiont.github.io/split-keyboards/)

### pchristensen (karma=12683)
* [http://www.pchristensen.com](http://www.pchristensen.com)

### kentonv (karma=12667)
* [https://cloudflareworkers.com](https://cloudflareworkers.com)
* [https://capnproto.org](https://capnproto.org)
* [https://Sandstorm.io](https://Sandstorm.io)
* [https://sandstorm.io](https://sandstorm.io)
* [https://developers.google.com/protocol-buffers/](https://developers.google.com/protocol-buffers/)
* [http://kentonsprojects.blogspot.com/2011/12/lan-party-optimized-house.html](http://kentonsprojects.blogspot.com/2011/12/lan-party-optimized-house.html)

### gjm11 (karma=12586)
* [http://www.mccaughan.org.uk/g/](http://www.mccaughan.org.uk/g/)
* [https://pobox.com](https://pobox.com)

### chatmasta (karma=12574)
* [https://www.splitgraph.com](https://www.splitgraph.com)
* [https://www.splitgraph.com/connect](https://www.splitgraph.com/connect)
* [https://www.notion.so/Splitgraph-is-Hiring-25b42164f0f5469eb1278899b543eb93](https://www.notion.so/Splitgraph-is-Hiring-25b42164f0f5469eb1278899b543eb93)

### csomar (karma=12560)
* [https://omarabid.com](https://omarabid.com)
* [https://omarabid.com](https://omarabid.com)

### lettergram (karma=12427)
* [https://insideropinion.com](https://insideropinion.com)
* [http://agw.io](http://agw.io)
* [https://austingwalters.com](https://austingwalters.com)
* [https://agw.io](https://agw.io)
* [https://insideropinion.com](https://insideropinion.com)
* [https://hnprofile.com](https://hnprofile.com)
* [https://redditprofile.com](https://redditprofile.com)
* [https://projectpiglet.com](https://projectpiglet.com)
* [https://lettergram.net](https://lettergram.net)
* [https://easy-a.net](https://easy-a.net)

### Arathorn (karma=12422)
* [https://Matrix.org](https://Matrix.org)
* [https://element.io](https://element.io)

### kirubakaran (karma=12173)
* [https://histre.com/collections/o34gelgt/kirubakarans-hacker-news-upvotes/](https://histre.com/collections/o34gelgt/kirubakarans-hacker-news-upvotes/)
* [https://kirubakaran.com](https://kirubakaran.com)
* [https://histre.com/](https://histre.com/)
* [https://kirubakaran.com/txt/pgp.txt](https://kirubakaran.com/txt/pgp.txt)

### lacker (karma=12115)
* [https://lacker.io/physics/2022/01/21/looking-for-aliens.html](https://lacker.io/physics/2022/01/21/looking-for-aliens.html)

### chubot (karma=12105)
* [http://www.oilshell.org](http://www.oilshell.org)

### jkuria (karma=12084)
* [https://CapitalandGrowth.org](https://CapitalandGrowth.org)

### pmorici (karma=12062)
* [http://therandombit.blogspot.com/](http://therandombit.blogspot.com/)

### alexandros (karma=11979)
* [https://resin.io](https://resin.io)
* [https://alexandros.balena.io](https://alexandros.balena.io)

### baby (karma=11962)
* [https://Cryptologie.net](https://Cryptologie.net)

### akkartik (karma=11954)
* [http://akkartik.name/about](http://akkartik.name/about)
* [http://akkartik.name/lines.html](http://akkartik.name/lines.html)

### JacobAldridge (karma=11895)
* [https://jacobaldridge.com](https://jacobaldridge.com)

### egypturnash (karma=11881)
* [http://egypt.urnash.com/rita/](http://egypt.urnash.com/rita/)

### FabHK (karma=11834)
* [http://www.fabian-lischka.de](http://www.fabian-lischka.de)

### codegeek (karma=11825)
* [https://yashchandra.com](https://yashchandra.com)

### sahin (karma=11702)
* [https://RemoteTeam.com](https://RemoteTeam.com)

### bko (karma=11700)
* [https://mleverything.substack.com](https://mleverything.substack.com)

### neilk (karma=11667)
* [http://neilk.net/](http://neilk.net/)

### davidgerard (karma=11619)
* [http://davidgerard.co.uk/blockchain/](http://davidgerard.co.uk/blockchain/)

### exolymph (karma=11569)
* [https://www.sonyasupposedly.com](https://www.sonyasupposedly.com)
* [https://www.reddit.com/r/sonyasupposedly/](https://www.reddit.com/r/sonyasupposedly/)

### brlewis (karma=11554)
* [https://en.howtruthful.com/](https://en.howtruthful.com/)

### sytse (karma=11453)
* [https://about.gitlab.com/](https://about.gitlab.com/)
* [http://sytse.com/](http://sytse.com/)

### ChrisArchitect (karma=11444)
* [http://www.cbldatarecovery.com](http://www.cbldatarecovery.com)

### michaelbuckbee (karma=11423)
* [https://expeditedsecurity.com](https://expeditedsecurity.com)

### donatj (karma=11254)
* [https://donatstudios.com](https://donatstudios.com)

### amirmc (karma=11242)
* [http://amirchaudhry.com](http://amirchaudhry.com)
* [https://https://docker.com](https://https://docker.com)
* [http://unikernel.com](http://unikernel.com)
* [https://http://nymote.org](https://http://nymote.org)
* [https://https://mirage.io](https://https://mirage.io)
* [https://http://www.springboard.com](https://http://www.springboard.com)
* [https://http://www.tidepowerd.com](https://http://www.tidepowerd.com)

### Jaruzel (karma=11237)
* [https://mattowen.com](https://mattowen.com)
* [http://jaruzel.com](http://jaruzel.com)
* [https://hnbadges.netlify.app/?user=Jaruzel](https://hnbadges.netlify.app/?user=Jaruzel)

### ken (karma=11186)
* [https://freerobotcollective.com](https://freerobotcollective.com)

### Macha (karma=11142)
* [https://initprogram.com](https://initprogram.com)

### rustoo (karma=11059)
* [https://about.me/rustoo](https://about.me/rustoo)

### varjag (karma=11050)
* [http://funcall.org](http://funcall.org)

### pnathan (karma=11034)
* [https://ciq.co/](https://ciq.co/)
* [http://articulate-lisp.com](http://articulate-lisp.com)

### shakna (karma=11026)
* [https://shatterealm.netlify.app/](https://shatterealm.netlify.app/)
* [https://www.reddit.com/r/thethirdcave/comments/k4ess9/rthethirdcave_lounge/](https://www.reddit.com/r/thethirdcave/comments/k4ess9/rthethirdcave_lounge/)

### JohnTHaller (karma=11004)
* [https://JohnHaller.com](https://JohnHaller.com)

### marban (karma=10987)
* [https://upstract.com](https://upstract.com)
* [https://biztoc.com](https://biztoc.com)

### dewey (karma=10976)
* [https://getbirdfeeder.com](https://getbirdfeeder.com)
* [https://editorialsync.com](https://editorialsync.com)
* [https://annoying.technology](https://annoying.technology)
* [https://blog.notmyhostna.me](https://blog.notmyhostna.me)

### nickjj (karma=10955)
* [https://nickjanetakis.com/](https://nickjanetakis.com/)

### BinaryIdiot (karma=10954)
* [http://www.msngrjs.com/](http://www.msngrjs.com/)

### blowski (karma=10954)
* [https://da.nblo.ws](https://da.nblo.ws)

### Eliezer (karma=10921)
* [http://yudkowsky.net/](http://yudkowsky.net/)

### yardie (karma=10887)
* [http://www.joechin.com](http://www.joechin.com)

### abstractbill (karma=10853)
* [http://abstractnonsense.com](http://abstractnonsense.com)

### chrischen (karma=10738)
* [https://Instapainting.com](https://Instapainting.com)

### fcambus (karma=10724)
* [https://www.cambus.net](https://www.cambus.net)

### sbierwagen (karma=10713)
* [http://sam.bierwagen.me/](http://sam.bierwagen.me/)

### ThePhysicist (karma=10666)
* [http://kiprotect.com](http://kiprotect.com)

### rsynnott (karma=10654)
* [http://myblog.rsynnott.com/](http://myblog.rsynnott.com/)

### speeder (karma=10584)
* [http://gitlab.com/u/speeder1](http://gitlab.com/u/speeder1)
* [http://coderofworlds.com](http://coderofworlds.com)
* [http://www.abril.com.br/blog/campus-party/2011/01/19/fanatico-por-jogos-leva-seu-proprio-fliperama-para-a-arena/](http://www.abril.com.br/blog/campus-party/2011/01/19/fanatico-por-jogos-leva-seu-proprio-fliperama-para-a-arena/)
* [https://www.kidoteca.com](https://www.kidoteca.com)

### tempestn (karma=10555)
* [https://autotempest.com](https://autotempest.com)

### Vivtek (karma=10494)
* [https://vivtek.com](https://vivtek.com)
* [http://semantic-programming.blogspot.com](http://semantic-programming.blogspot.com)

### geuis (karma=10465)
* [http://geuis.com](http://geuis.com)
* [http://jsonip.com](http://jsonip.com)

### tel (karma=10446)
* [https://jspha.com](https://jspha.com)

### nkoren (karma=10419)
* [http://www.podaris.com/](http://www.podaris.com/)
* [http://www.futurescaper.com/](http://www.futurescaper.com/)

### cjbprime (karma=10375)
* [https://gittorrent.org](https://gittorrent.org)
* [https://printf.net/](https://printf.net/)

### moron4hire (karma=10351)
* [http://www.seanmcbeth.com](http://www.seanmcbeth.com)

### jackgavigan (karma=10337)
* [http://jackgavigan.com/](http://jackgavigan.com/)

### wmeredith (karma=10311)
* [https://WadeMeredith.com](https://WadeMeredith.com)

### hardwaresofton (karma=10270)
* [https://vadosware.io](https://vadosware.io)
* [https://unvalidated-ideas.vadosware.io](https://unvalidated-ideas.vadosware.io)
* [https://waaard.com](https://waaard.com)
* [https://loginwithhn.com](https://loginwithhn.com)
* [https://nimbusws.com](https://nimbusws.com)
* [https://surplusci.com](https://surplusci.com)

### zitterbewegung (karma=10261)
* [http://joshuajherman.com](http://joshuajherman.com)

### jakelazaroff (karma=10254)
* [https://jake.nyc](https://jake.nyc)

### joshfraser (karma=10248)
* [http://www.originprotocol.com](http://www.originprotocol.com)
* [https://www.onlineaspect.com/about/](https://www.onlineaspect.com/about/)
* [https://www.onlineaspect.com/contact/](https://www.onlineaspect.com/contact/)

### kristopolous (karma=10200)
* [https://getpostdelete.com](https://getpostdelete.com)

### soneca (karma=10194)
* [https://writingfordevelopers.substack.com/](https://writingfordevelopers.substack.com/)

### moultano (karma=10188)
* [http://moultano.wordpress.com/](http://moultano.wordpress.com/)
* [https://play.google.com/store/search?q=com.silvaspira](https://play.google.com/store/search?q=com.silvaspira)

### mintplant (karma=10169)
* [https://spinda.net](https://spinda.net)

### mattowen_uk (karma=10168)
* [http://www.mattowen.com](http://www.mattowen.com)
* [http://www.jaruzel.com](http://www.jaruzel.com)

### raphlinus (karma=10161)
* [https://raphlinus.github.io/](https://raphlinus.github.io/)

### Osiris (karma=10156)
* [http://batterybarpro.com](http://batterybarpro.com)

### SEJeff (karma=10111)
* [http://envisionlinux.com/blog](http://envisionlinux.com/blog)
* [http://digitalprognosis.com/resume.htm](http://digitalprognosis.com/resume.htm)

### burntsushi (karma=10108)
* [https://burntsushi.net](https://burntsushi.net)

### vog (karma=10089)
* [https://njh.eu](https://njh.eu)

### pier25 (karma=10086)
* [https://pierbover.com/](https://pierbover.com/)
* [https://wavekit.app/](https://wavekit.app/)

### dbaupp (karma=10083)
* [http://huonw.github.io/](http://huonw.github.io/)

### ben_w (karma=10072)
* [https://Brilliant.org](https://Brilliant.org)
* [https://kitsunesoftware.com](https://kitsunesoftware.com)

### mturmon (karma=10063)
* [http://turmon.org](http://turmon.org)

### mwcampbell (karma=10028)
* [http://mwcampbell.us/blog/](http://mwcampbell.us/blog/)

