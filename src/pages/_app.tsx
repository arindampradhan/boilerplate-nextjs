import '../styles/globals.css';
import type { AppProps } from 'next/app';
import { appWithTranslation } from 'next-i18next';
import { wrapper } from '../store';

function MyApp({ Component, pageProps }: AppProps): JSX.Element {
  return <Component {...pageProps} />;
}

const MyTranslatedApp = appWithTranslation(MyApp);
const MyReduxApp = wrapper.withRedux(MyTranslatedApp);

export default MyReduxApp;
