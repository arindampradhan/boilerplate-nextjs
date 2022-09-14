// more declarations
// FIXME: type defination not working
//
declare module 'components/**/*.svg' {
  import React from 'react';
  const Component: React.FunctionComponent<React.SVGProps<SVGAElement>>;
  export default Component;
}
