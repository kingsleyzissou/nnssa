module.exports = {
  title: 'NNSSA',
  tagline: 'Neural Network Based Song Structure Analysis',
  url: 'https://kingsleyzissou.github.io/nssa/',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'kingsleyzissou', // Usually your GitHub org/user name.
  projectName: 'kingsleyzissou.github.io', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'NNSSA',
      // logo: {
      //   alt: 'Logo',
      //   src: 'img/logo.svg',
      // },
      items: [
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        { to: 'blog', label: 'Blog', position: 'left' },
        {
          href: 'https://github.com/kingsleyzissou/nnssa',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Style Guide',
              to: 'docs/',
            },
            {
              label: 'Second Doc',
              to: 'docs/doc2/',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: 'blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/kingsleyzissou/nnssa',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Kingsleyzissou`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/kingsleyzissou/nnssa/edit/master/website/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/kingsleyzissou/nnssa/edit/master/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
