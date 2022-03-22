// https://gist.github.com/thesnappingdog/64ac3c4207fc539e3e44e06afae6aa69

// Copy this code to your custom code module.

const axios = require('axios');

exports.main = async (event, callback) => {
  const website = event.inputFields['website'];

  // Replace this with your own API url! The heroku example is slow and limited ;)
  const domainApiUrl = 'https://url-to-domain.herokuapp.com/extract';

  let domain;

  try {
    const result = await axios.get(domainApiUrl, { params: { url: website } });
    domain = result.data.domain;
  } catch (error) {
    throw error;
  }

  callback({
    outputFields: {
      website: website,
      domain: domain,
    },
  });
};
