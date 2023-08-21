---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
  - block: collection
    id: publications
    content:
      title: Recent Publications
      text: |-
        {{% callout note %}}
        Quickly discover relevant content by [filtering publications](./publication/).
        {{% /callout %}}
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: citation
  - block: portfolio
    id: projects
    content:
      title: Projects
      filters:
        folders:
          - project
      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
      default_button_index: 0
      # Filter toolbar (optional).
      # Add or remove as many filters (`filter_button` instances) as you like.
      # To show all items, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the toolbar, delete the entire `filter_button` block.
      buttons:
        - name: Recent
          tag: recent
        - name: Old
          tag: old
        - name: All
          tag: '*'
        
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
      view: compact
      # For Showcase view, flip alternate rows?
      flip_alt_rows: false
  - block: markdown
    id: teaching
    content:
      title: Teaching
      subtitle: ''
      text: |-
        **Current courses**
        * [Programming Languages](https://github.com/jacopoMauro/dm552),
          University of Southern Denmark
        * [Microservices & Dev(Sec)Ops](https://github.com/jacopoMauro/dm874),
          University of Southern Denmark

        **Topics available for Master Thesis**
        * Dev(Sec)Ops & Cloud Computing
        * Optimization
        * Algorithm Selection
        * Constraint based AI Explanation
        * Formal Methods
        * Choreographic programming
    design:
      columns: '2'
  - block: markdown
    id: awards
    content:
      title: Awards
      subtitle: ''
      text: |-
        * [Innovation Prize](https://acp.sdu.dk/news/2022-08-25-Mauro-Innovation-Prize.html) from the Faculty of Natural Sciences - University of Southern Denmark (2022)
        * [Silver medal at the MiniZinc Challenge](http://www.minizinc.org/challenge.html), i.e., the international competition of constraint solvers (2020, 2019, 2018)
        * [Gold medal at the MiniZinc Challenge](http://www.minizinc.org/challenge.html) (2017, 2016, 2015)
        * [Best Algorithms Selector for runtime minimization at Open Algorithm Selection Challenge](https://www.coseal.net/open-algorithm-selection-challenge-2017-oasc/) (2017) 
        * [Best doctoral dissertations of 2010-2012](http://www.programmazionelogica.it/2011/08/distinguished-dissertations-2010-2011) (2012)
        by the Italian Association for Logic Programming
        * [Best doctoral dissertations of 2012](http://eatcs.org/index.php/italian-chapter-awards) by the Italian Chapter of 
        EATCS (2012)
    design:
      columns: '2'
  - block: markdown
    id: links
    content:
      title: Other Links
      subtitle: ''
      text: |-
        **Software**
        * [SUNNY-CP](https://github.com/jacopoMauro/sunny-cp): a portfolio based constraint solver
        * [mzn2feat](https://github.com/jacopoMauro/mzn2feat): a feature extractor for MiniZinc/XCSP files

        **Discontinued software**
        * [Zephyrus2](https://bitbucket.org/jacopomauro/zephyrus2): an optimal deployment configurator
        * [HyVarRec](https://github.com/HyVar/hyvar-rec): a context-aware reconfiguration for Software Product Lines
        * [XCSP-to-MiniZinc](http://www.minizinc.org/resources.html): a file converter form XCSP to MiniZinc

        **Chocolate experiments**
        * [Nutella: US vs Europe, experiment report](papers/nutella_experiment.pdf)
        * [Nutella: Australia vs Europe, experiment report](papers/nutella_2019.pdf)
    design:
      columns: '2'
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      # text: |-
      #   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam mi diam, venenatis ut magna et, vehicula efficitur enim.
      # Contact (add or remove contact options as necessary)
      email: mauro.jacopo@gmail.com
      pemail: mauro@imada.sdu.dk
      phone: +45 65 50 25 72
      # appointment_url: 'https://tinyurl.com/y9rz4lyb'
      address:
        street: |-
          Department of Mathematics and Computer Science,<br>
          University of Southern Denmark,<br>
          Campusvej 55, Odense M, 5230, Denmark
        # city: Odense M
        # region: CA
        # postcode: '5230'
        # country: Denmark
        # country_code: US
      office: 
      directions: Office number Ø13-604a-2. You can locate it using the <a href="https://tinyurl.com/y9rz4lyb">SDU online map</a>.
      office_hours:
        - by e-mail appointment
      # contact_links:
      #   - icon: twitter
      #     icon_pack: fab
      #     name: DM Me
      #     link: 'https://twitter.com/Twitter'
      #   - icon: skype
      #     icon_pack: fab
      #     name: Skype Me
      #     link: 'skype:echo123?call'
      #   - icon: video
      #     icon_pack: fas
      #     name: Zoom Me
      #     link: 'https://zoom.com'
      # Automatically link email and phone or display as text?
      autolink: true
      # Email form provider
      # form:
      #   provider: netlify
      #   formspree:
      #     id:
      #   netlify:
      #     # Enable CAPTCHA challenge to reduce spam?
      #     captcha: false
    design:
      columns: '2'
---
