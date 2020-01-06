const apiUrl = (path: string): string =>
  `${process.env.API_URL}${path}`;

export {
    apiUrl,
};
