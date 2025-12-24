// @ts-check
import { themes as prismThemes } from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'An AI-Native Technical Textbook',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://physical-ai-textbook.vercel.app', // Vercel deployment URL
  // Set the /<base> pathname under which your site is served
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  // organizationName: 'Governor-Sindh-AI-Course', // Usually your GitHub org/user name.
  // projectName: 'Physical-AI-Textbook', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Remove this to remove the "edit this page" links.
          editUrl: 'https://github.com/Governor-Sindh-AI-Course/Physical-AI-Textbook/edit/main/',
        },
        blog: false, // Disable blog functionality
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'light',
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },
      // Replace with your project's social card
      image: 'img/physical-ai-social-card.jpg',
      navbar: {
        title: 'Physical AI & Humanoid Robotics',
        logo: {
          alt: 'Physical AI & Humanoid Robotics Textbook',
          src: 'img/logo.png',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Textbook',
          },
          {
            href: 'https://github.com/Governor-Sindh-AI-Course/Physical-AI-Textbook',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Textbook',
            items: [
              {
                label: 'Introduction',
                to: '/docs/intro',
              },
              {
                label: 'Module 1: Foundations',
                to: '/docs/module-1-foundations/intro',
              },
              {
                label: 'Module 2: ROS 2',
                to: '/docs/module-2-ros/intro',
              },
              {
                label: 'Module 3: Simulations',
                to: '/docs/module-3-simulations/intro',
              },
            ],
          },
          {
            title: 'Resources',
            items: [
              {
                label: 'GitHub Repository',
                href: 'https://github.com/Governor-Sindh-AI-Course/Physical-AI-Textbook',
              },
              {
                label: 'Issues',
                href: 'https://github.com/Governor-Sindh-AI-Course/Physical-AI-Textbook/issues',
              },
              {
                label: 'Contributing',
                href: 'https://github.com/Governor-Sindh-AI-Course/Physical-AI-Textbook/blob/main/CONTRIBUTING.md',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Governor Sindh AI Course',
                href: 'https://governorsindh.ai',
              },
              {
                label: 'Docusaurus',
                href: 'https://docusaurus.io',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Governor of Sindh AI Course. All rights reserved. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;