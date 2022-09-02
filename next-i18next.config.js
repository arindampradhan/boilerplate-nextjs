const DEBUG = 0;

module.exports = {
  // https://www.i18next.com/overview/configuration-options#logging
  debug: DEBUG && process.env.NODE_ENV === 'development',
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'es']
  },
  fallbackLng: {
    default: ['en'],
    'es-ES': ['es']
  },
  // localePath,
  reloadOnPrerender: DEBUG && process.env.NODE_ENV === 'development'
};
