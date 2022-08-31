const DEBUG = 0;

module.exports = {
  // https://www.i18next.com/overview/configuration-options#logging
  debug: DEBUG && process.env.NODE_ENV === 'development',
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr']
  },
  fallbackLng: {
    default: ['en'],
    'de-CH': ['fr']
  },
  // localePath,
  reloadOnPrerender: DEBUG && process.env.NODE_ENV === 'development'
};
