import React from 'react';
import '../styles/globals.css';
import type { AppProps, NextWebVitalsMetric } from 'next/app';
import { appWithTranslation } from 'next-i18next';
import { wrapper } from '@/store/index';

export function reportWebVitals(metric: NextWebVitalsMetric) {
  const DEBUG_WEB_VITALS = 0;
  // eslint-disable-next-line no-console
  DEBUG_WEB_VITALS && console.log(metric);
}

function MyApp({ Component, pageProps }: AppProps): JSX.Element {
  return <Component {...pageProps} />;
}

const MyTranslatedApp = appWithTranslation(MyApp);
const MyReduxApp = wrapper.withRedux(MyTranslatedApp);

export default MyReduxApp;
