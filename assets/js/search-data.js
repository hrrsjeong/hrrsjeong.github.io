// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "Home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-team",
          title: "Team",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/people/";
          },
        },{id: "nav-research",
          title: "Research",
          description: "Research directions in primate and human evolution, pangenome structural diversity, single-cell epigenetic aging, and computational and AI methods at the Jeong Lab.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research/";
          },
        },{id: "nav-publications",
          title: "Publications",
          description: "Preprints and peer-reviewed publications from the Jeong Lab.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-join",
          title: "Join",
          description: "Opportunities for postdocs, graduate students, bioinformatics specialists, and undergraduate researchers at the Jeong Lab at GIST.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/join/";
          },
        },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "news-the-jeong-lab-officially-opens-its-doors",
          title: 'The Jeong Lab officially opens its doors.',
          description: "",
          section: "News",},{id: "news-강동균-류다영-and-이영서-join-the-jeong-lab-as-undergraduate-researchers-welcome-to-the-lab",
          title: '강동균, 류다영, and 이영서 join the Jeong Lab as undergraduate researchers. Welcome to...',
          description: "",
          section: "News",},{id: "news-dr-jaewoong-lee-joins-the-jeong-lab-as-a-postdoctoral-researcher-welcome",
          title: 'Dr. Jaewoong Lee joins the Jeong Lab as a postdoctoral researcher. Welcome!',
          description: "",
          section: "News",},{id: "news-dr-hyeongwoo-choi-has-joined-the-jeong-lab-as-a-postdoctoral-researcher-welcome",
          title: 'Dr. Hyeongwoo Choi has joined the Jeong Lab as a postdoctoral researcher. Welcome!...',
          description: "",
          section: "News",},{id: "news-our-single-cell-dna-methylome-study-is-now-published-in-nature-aging-congrats",
          title: 'Our single-cell DNA methylome study is now published in Nature Aging. Congrats!',
          description: "",
          section: "News",},{id: "news-sooyeon-lim-and-juyoung-kim-join-the-jeong-lab-as-undergraduate-researchers-welcome-to-the-lab",
          title: 'Sooyeon Lim and Juyoung Kim join the Jeong Lab as undergraduate researchers. Welcome...',
          description: "",
          section: "News",},{id: "news-our-lab-has-been-awarded-computing-allocation-through-the-kisti-national-supercomputer-no-6-r-amp-amp-d-innovation-program",
          title: 'Our lab has been awarded computing allocation through the KISTI National Supercomputer No....',
          description: "",
          section: "News",},{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/hrrsjeong", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/hyeonsoo-harris-jeong", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=Bw9m8r8AAAAJ", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
