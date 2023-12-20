from frost_mpc.common.libp2p_protocols import PROTOCOLS_ID
VALIDATED_CALLERS = {
    '16Uiu2HAmGVUb3nZ3yaKNpt5kH7KZccKrPaHmG1qTB48QvLdr7igH': [PROTOCOLS_ID['round1'], PROTOCOLS_ID['round2'], PROTOCOLS_ID['round3'], PROTOCOLS_ID['generate_nonces'], PROTOCOLS_ID['sign']]
}

SECRETS = {'16Uiu2HAkv3kvbv1LjsxQ62kXE8mmY16R97svaMFhZkrkXaXSBSTq': '7f31124800890e662580f2b3fcac0b6200f1a7d9dc343bef6cbea8e9e02a5a5b',
           '16Uiu2HAkvumPB54FCBoNR8nh4aVBNhdv8sNAtt6GegL6aW2V5nCe': '7e07c2a9242a4ac6ca0f3deb65f3154483c739862bc1ca8bff1f914c4b87da0c',
           '16Uiu2HAkw89MG4Myh5hitNPVTqPekkCwMzib4Jq6BD9rtQLvJSPy': 'd6862a78d7f89d9276c7722fd860b9e4d1a0e6b04f3cc38934e7fce4dcf404b3',
           '16Uiu2HAkwAnCC6DunFsXvARa2pHSFJaQNAXbPntjxbEyFRsSzGSW': '2dab3dbf272fe8446381e6870d1cd11851679e1222a41d6bfd475282f9426e19',
           '16Uiu2HAkwDW3SKiofh5ypLxVVGsenzabbHjE9NzxhoxK8rpGw4mg': 'cccd723d9126349d6873384c44fba484c193ccd52ce4de1cb8b5e9be0843b5c3',
           '16Uiu2HAkwQ2NWsPszoeNkaMX4o3VV6rqb7b4AsVvJsw8jLMtvR1r': 'c35cb145b119abb28cb8dd125d6bac254cfbd9ecc32d25be2878c186f3b2a9e8',
           '16Uiu2HAkwZuuxHZBvUDV4XLe54vDEBUM5SmNNmVb9As9EzJmDKZN': '0c18ff58eaec60deb3577c6a33a4c7a5d0c108c1e228e6832e52725e67b0eae1',
           '16Uiu2HAkx3HYEfKJZWp3gnxParDEs4SosH9bx2aJUSaxQtkLgyvf': '433291b8a233ffd79584dad6d69b8dc48ff2496259d65ea6ca799b776bd2b5c2',
           '16Uiu2HAkxJNxQaXhftygPW8NZgHwNjfRgqeXCBGUmooun2hNrnAo': '74c754cb2a19953dead9dbdaeb4722e975f58a78890b93f08a23e015f5e4f98a',
           '16Uiu2HAkxw3mLEidfSmUEecN7cwcXd9gkzgr1D4LPeaEbJkbA8w6': 'e2ab7f926d029eb7d6b49afbdf0f17904bc628d1e9bd48b8f27ec8e6f29a92e9',
           '16Uiu2HAkyY6N9LdJdmSELymYHFEuyvHphHheDRPZE8bpX5LWSZ3x': '96df0d6f6c5006610e0137a3bb1e5830ca124021dd5d09fa06a6bd81d4c9bbbb',
           '16Uiu2HAkysXuPfw7w2JXXG73aYJemjYAMCmeytDsi7JQLzKqdisk': '6154b721e0660a99555ef697aee0f98fedc8d51d6f5a475149cbf33083341617',
           '16Uiu2HAkyyJgoSzyvnEGXsJxZARKHpryNRPJqX2DxqMVwq53NxQQ': '0aba564c9fa404c6db9870125ca4ddd470c55ac54534e83db33e93582fa858a1',
           '16Uiu2HAkz6vRNGh6gobuK64EgcTopQU8cEaQ5AYUu2JGiMi6tJux': '6731b633ec7cd653613fef00519e643f401ec89836cd9c23e80313d3922f1196',
           '16Uiu2HAkzhvUZHCmBiFDEPmfD9JJFdagbNMdku2dCZgZYeQAHFQF': 'a5a6ee6a6483cdb5a4b68d3a2bddf11d4d291c44771a59055d6b2b5601b5a83a',
           '16Uiu2HAkzyAGdeUp7sGQS8Rr8wKbbjHJFYjgigQVAN2KSRoC79nD': '03c8463be423bab9dd83737fcb1a3bc20ce05baa544f2c5d85f91bb754b9cec2',
           '16Uiu2HAm1nPv2nUQAbzKEmNLxjXQtkp3BHpB2Hf8MZRZ1NktCwh7': '4b02a4fe373d2d0bfb19b40a5fbc76986e950eadae2a3c3cb063f57ae4284509',
           '16Uiu2HAm38JiV84kg9CGyMuicNbQJvFSuhbyuSeZaAi9ZNnqysjQ': 'd6849131729027a4414b3164861a81948ad8d831f2e53bcb56e210c07684bbda',
           '16Uiu2HAm3Be3qSoam2r2WWgL1CFoWAm79Y6y12jydmaQikKvuNMB': 'ec23e69f106fd1deacae4e2b1bf3642fff436bb421dace08c93a515e563e1a4a',
           '16Uiu2HAm3bYN4xcyXdNBAAhTeDXVfrePUEfkzdVSWNtC66hdKmfe': '5ae202cd35295e359863bb8fbd8984565806997ed960960a9e73d1034ba4fe2e',
           '16Uiu2HAm3pChJeFoz5TqreVbUkL8pzBzooJ8A1oFjnpfX15eYe4G': 'dea4c248d3aecbb356d11a38af2ef78baf943fe5e172e2beb26412105ca4752a',
           '16Uiu2HAm46gwTUqQFRGKfJyQeHbkk51AjREGRJVPXvWRmHyZbAaV': 'c5e2e374f9066f53cdded8a6cd71c48953510b5ca89f8b7b36c49a49e6e921d4',
           '16Uiu2HAm4DuQ724pJUW2kpR7w38Gx4YHLCJ6Ypuha5GgVBSBc1w1': '6c0262c3c12ccef130e26a4b890407f7cd1d2e6c3beae84519c171d0194acfdc',
           '16Uiu2HAm5XnWNQmUbT9u2ACdWRkZvEukvXQMFW7rGAQnq8YwNsVD': '5190491672f731a381682cdebc902c1d1a13f4d4d30f4a9ee080d24c4eb50ccb',
           '16Uiu2HAm6jQnooavM9g2oX7n3FaBgX6TJuTAAS9MgW5ebVwQvVCp': '877a20bb10c8bbc808cc0fe7f4e71e8d36ba98a5a8aa237d3bfe01a6129046fb',
           '16Uiu2HAm6pgCcFaJ4LcBdCivRWAk9ZTSpKw8zGr79AZkwCEyADT1': '4e1ae7543191b61fa0f87b710b272714babda9edf515fc185b98cb357b5552d5',
           '16Uiu2HAm72WKcREmDtTgNeZEkbG2Gc1x4duhUeH7s6cSNTX1xsVA': '2f0ada15152d38406f45e69671172aaae624816bcf930e6b1dd36c73493d573e',
           '16Uiu2HAm76CXkZTnpCkAUD5Ze4BivcebHGtzxsHVUpgM31qH4fZo': '9e2e5ebe606b16b5028a82986e757a51b2ece888b1d6c8e5002e4df94da7e70c',
           '16Uiu2HAm77TDp3uNrkh7yirmgmk19AEHCsH3maxsrPn78Z7iTMax': 'f61e1c080e7608521d053e53642d6bff7befcf6a7539273fa95c125788bd3cbc',
           '16Uiu2HAm7vnKNw1dSy549vdVhvY1zgkujC68n3eHeynwzSBZpMSv': 'c0a758d2c9f8cdccedfd2d382cc89ab84600a18d92359381a482c7040a15f87a',
           '16Uiu2HAm8AnZ2CqqkNRn9nptQ4uYzVYakscVZSNuV5XvSKTAeM7t': '2d756bf065aa9b80c39c1927744d344d34e7f799549202e1a57a0dc7e441f52a',
           '16Uiu2HAm8JJwBQrhgFDe3FNav97wuZDCVYW9XRLbTaETTV28hbmd': '289c6235d6e1168190d58f4b0bb98b42ed2a7cf1d6a28aa7e26e5352a7427787',
           '16Uiu2HAm8UUfbxxXa2dorkjdR33dFGdseNCP45oegrsgNfpx9Whu': '3cf8070ef5c7e1495b3ee0fe77e6227c3e394f8dec3185024952b1d5fbf8295c',
           '16Uiu2HAm8Z9DJtSTTXodtoebJx2NyJGQghytpnbo1AtFc9c9weEL': 'e40e6c623e89103fe9b811e5a1f2cef445810554a2852a7c27854fbb4710f7d3',
           '16Uiu2HAm8eaTYxTXFjG6g3ZA8QCMGuQ8PE4mCjiUJcuFGq97jJcg': '851f3a9d92ef600f508d017ded63f4f8d8d437fa9debbe5f6728e46d63c37ee4',
           '16Uiu2HAm8mU5RM5mMcEEDGE5omXYJzv5QRxN22cH1SBHwjuerRKj': '41076aa80a0ddef94df6e8dd1d17296b1f7b3461c5006fb48dc6eaaa5742c3ce',
           '16Uiu2HAm8oyrX2PDxExK3Xu4J2HeBEaLZmhoipbMp88LqEumkiRn': '16a02e0cf726fc9c10c32a4bb61773563c42e10785c338a02c47d5aec417c9e1',
           '16Uiu2HAm8yipjAyjBMtsJSsM3Skj6r6gGAowwZ4N33MH6PzwUgBV': 'bddb79c0d443e5d4ef452977697d56f4da1d1277ba126d12d966cffccfdda464',
           '16Uiu2HAm915vmRbxpE5UL9EFWtZK7SZRW9toexCZdhrgteSAxTkp': '9a368e6bf8d28795766ec4a4e52866d52574b857d99b3f91ccdee37e6b69ff7f',
           '16Uiu2HAm9D3NEzM6MybjELGkD1xyyUAZjH59Du6u3cQCRgHeLowN': '32ea0a58575fbb180b901c43fafb76084d45546be16653e476fd813ae84cc872',
           '16Uiu2HAm9rGvQe5gxbgDWDhCxpa5xx3x3k7hq4yDWKLZCy7yJk2m': '7fdc3a87dbf5714ba76c8491a48e15a8c3defea35fef5b5842606107dda91bc6',
           '16Uiu2HAm9zebzCft973E6jsbtiw1ZJ6tytdR7wZr7AVW2n6RaVYT': '3e2255410aaffdf365dfc8a2d539565eb0996fde29666f67e446dad21886d95e',
           '16Uiu2HAmBEnVWsVsHdfJSahmG84eX9msapCpCzdUQ4vuaE6gv6rV': '6c5ba7f8d362bed37f84c3877466dc54c304b56d43f19025d311ca72c5ce7083',
           '16Uiu2HAmBVy9HxHpm2TdN13rhgnuA8RckSV3e2Hn5b4agNgv7TJJ': '9e8233d81623ef30cc4d16ca09a11db33f443e0939201e0ded8f0c50f3276fa9',
           '16Uiu2HAmCUWfW1Gp6BpLG5GVdVVo4DWdZjebnYavHrKKP3QYnDKm': 'a2e61d2df82175c9168313ae572f76f8a1e4cfe250fe8905746f48c15b76b095',
           '16Uiu2HAmCW3a8Uecc67rqMd4DwbA3ueKAK92XnixQtnFFnfeJWsH': '5c055e0da9f4eceebeaad9abcbe3657aa577fcefcd10be8266d92f2f1ce63120',
           '16Uiu2HAmCXu2zYj1FCsF6u14wyKpXGgahQWfKEzktfspRHZq6YFN': '6063df6d9d0784ac3dcf917b416930b1f9154f4b27cbc33644401e789dd434d1',
           '16Uiu2HAmCptiqhC2HSrkw1WiNYBzCCQ4PDAn52WqD8BHraVGt91M': 'e4e073a0c317e223c91338b657096662efefd518a50d1b8fb9e0a3d03b1f0c8f',
           '16Uiu2HAmCq9jPmLaP7JhRWqaNxxPKuDR4Y4TwGY5h2stEgnXVD2R': '27d9d05e2eff9588788a3b668d7fc6da7b05d8ebfc41583b66d133ffdc09122b',
           '16Uiu2HAmE7bP2u1iTZSkYWkDLr6HEcMX5ieNPfZmWoLKctF2fAgb': '343357ccb4cb79bcc8c246c20ee59c6af871ec39840ad0b67cb55306cbc13bcf',
           '16Uiu2HAmEQ3vY1EoYLgEyDbqM1NCx9Fphcv9a5TriWeDtxXkBxJc': 'e5bde768199b6577ed5095d3799087111d7afd05d9a69c2f3458965b57caac39',
           '16Uiu2HAmEascgB9rXUz1gr9EfPzMt6xRuktvEQ85S18ZXPHLaFkf': 'd41f14f6bc457458fcbe6517cbf30c71c1afa6b8af405f215c0d9ef5f5317f33',
           '16Uiu2HAmFLG2CxzhXiGri6qaV7vtourQvr2txQ84MX3doLsgcwxi': '9097069d946c90a507c9e0dfe4592eec304796adb4070d08de0553212e2036d0',
           '16Uiu2HAmFQn5hLvh8qGADq84durPy3VHCc2GywbRVvMkYuLwekTW': '6e7d068f2a5f20cff7b879f9097ee1908c26a8efe3d2f306b29b00c57e359ece',
           '16Uiu2HAmFrk11qasauxSLNHn6ShwfK3SakcjARCggVxJQDr5zDRT': '37c45f868c26c15b13ada1d63ccfc17dfe40d3a3560010071a1f13a66ace85a2',
           '16Uiu2HAmGEttySjXB7PfUiheTjdm7K5H2W2gFXGXEnTsUob9a3HK': 'ff5b323da2c54dcb44dac744e540a1394af64791a44d0bd103d4d0edc19d2a19',
           '16Uiu2HAmGiH1LSULdoUnWt74tSzbid2W5UUGiEDw36LzErC7do7S': 'ae58b53da0fba5eabc719e432b3c494f0e99646f8d0d8ed0fa1e6191d3a0d67a',
           '16Uiu2HAmGkr7i2ohpEfvZRffSRD6e4Bb3ARn9ac8Fs35HYFbxXzu': 'e65b2cf601e23aa4921736c9198f3d0157a05084f3fbe1415c74c6af5aed972e',
           '16Uiu2HAmHNKKMJ44jzNpZLV8kHFK8DeNt61AMMqVhMug7wG4hboB': 'cdd6f553c95838c2dc98edf7f7dc83ac682944b4279ae3771aef7152802ffbe5',
           '16Uiu2HAmHfMMPHVH4k3UAXQsGritPxJSnwWMazP1D5rSnnfbWURm': 'fb88658c8d116064910a4c090f71dd2aa6b181009e5ae6b99c977a73a1997dd9',
           '16Uiu2HAmHiAuNMrbtWkpas7xmJGtL7BYWzP14mrANt4zVsV9NCtW': '996738d3f16049eda3b90e9bd03712d20998c70998946c601f3d2066b227044c',
           '16Uiu2HAmJ85ECrST7Z7ozh7Q1dztH5gGReK3yaCH5hUTxBotkuRe': 'cdf1ffe67696fdd34100c00caefbea56bcb9a5711b8168028cb17707d6c24c95',
           '16Uiu2HAmJH9zFv3AB46FCSM7x1Ja3dTsgYeY1GVTeE1Mwiozr5HV': 'f82056861529f3474c08fbf08cd44f8b4684ff63615c3f11aede26f8d502d835',
           '16Uiu2HAmJYPzYUt3FAdh2YD4hChNTYepECJrDGfNbKzWx3kKSMod': '1ef55ee69e7093093ba865643b051e782e9d9d8225503b133b388c982ffd5242',
           '16Uiu2HAmJcVZxKeooaiDkVEyPhRsdaRCCJgKbYryczJX1MdEHWGA': 'd8ad9b99a3f00f04ca220b131f8b275bbbe9955474ad30887f89eb1e07e102f6',
           '16Uiu2HAmK2wRLg7tECgNdk7Ycx2EkD2v7m2977tDBJtc2D9EtfEN': '5925bef14d89fb3c078d9f5ed6ccd249f960cafcf109d06d2bcb8225af70034a',
           '16Uiu2HAmKA5QQk5nUk93XBPWLeZLsFkfH6KjW9RRCeM5cjfKnYdm': '68b5ccf2974080dfd3596cdd062602895a365b2b12e916ecc2dc10acbdcad60b',
           '16Uiu2HAmKrkPHgb3EEv6ndUf83aFmXfMmKwYLd2RohSG56szJnLu': '0d508111acb23919f862f4b37d723dd4b4f43e43d44e175093b7479e131c5096',
           '16Uiu2HAmLNL2U7GFKLGFUeJB2Z6qQwT5gVHuk8QXr6VRh6kbuAY2': '82785ee65720a77450937388e119f5c99a2c83b86fbcd773a3ef298ba15724d3',
           '16Uiu2HAmLNje54UHd8b7jHZgZUhDfuaY9eG1zkNcWAEKNaMpjRLp': 'ff5bb72865f0b4a7805aadaa4c350410747a828e0d5ed1be487e20b2fb376d50',
           '16Uiu2HAmLYD6Rg8Wxfg5PDtxiRDiS1mEAN5XApJtgLG7qzuFuH8M': '03a24eeef5b550842c11670397eb6b1fb9db2dcc4adbd0506d2c3c4ddbb9a8e3',
           '16Uiu2HAmLskVaF1BFUZMeTE96bCsFJJoeXHCkpLFGPD86uXpizHc': '4da4086cb85f30cfe7f08267117c0455374d7530972ffaf1c53d636b6b4d0876',
           '16Uiu2HAmMwFYBVQSmBUq1Y8XWnE3x5fm6Hwfsj6vKRZnyST7CTPQ': '6b8b8952ee9a649bbefd736f905dc6d655831e374d183b22fc35bf929ea3bb3c',
           '16Uiu2HAmNXzrwsofwKoseR6SQcQDpghWg6tW7upDwLYrwdzh34S5': 'f91638eace558828f1bc509eb14d117f916931da16aab4ae82f7226f532e5419',
           '16Uiu2HAmNgv3yCUiaapWueMWKw672KSovQ17W6TwKUxGQPYZqA9X': '288d0956401cb0b47c6f5bdde099b5cfbe3a5db14ff3bd5a4606434f762235eb',
           '16Uiu2HAmNmLZSmzvWxdXut5jaPJKYdErwDxd9q9EsZ3g9yVK6tFQ': '3bc2b1e0d2eb460cce347ab3d5c00e8dfc8bd3394e27b8d517b787dd566b40e2',
           '16Uiu2HAmPWa48jxrHBf1AmC96fKsdavxiMsS41JchjygNcKKyozU': 'f7cdac3cc5f54ef61e83151d4fbee38133e90c3e5de9e17b72876471626b6764',
           '16Uiu2HAmPi9yVmEca5mfShk3Mkx9vJyjoqovmqY5vTTZ9pxwfMu3': 'aeb9d66aaae37bed23dee3cc4b6a2991bebf10bd0fbcec701a0adc587b660949',
           '16Uiu2HAmPkBGbfqVJWFuQ6daPD3ADEhHR88pSXnEoTQMe1w81e2m': 'c2d42eb9b000971682123cc1cb749b18385220a71d191b3f70108d4fdb33978d',
           '16Uiu2HAmQ1xwiSahCYuVhjVTuVxHC6Uywmx5FApdEeNyh6DSBFuy': 'baf3bef35780e473aeefd14b71f422449ff1c80bbb938933a03f55c6743dd49c',
           '16Uiu2HAmQE5c8e7YkkT92YQJwCw6DFxD1b3XZtNFCShQdixFJy9J': '44de71bcca88523e39ad39fb21f94e5362d013176744b72827af6a7f35b51b81',
           '16Uiu2HAmQfQXir7c4ibJFh9guSAoYj3wERnCG7hjuS3N1Qusbcx6': '0a57704389e88c1a410a1871420ea5a9a0fd3f7a31f033cb84a7da4b4171f02e',
           '16Uiu2HAmRFWBqDr1VrMNKboSQAUpHEcNGxhs199tEu4YBofpzEES': '6a8210ca42edf2e90e3bcf0e36e2ed1e8cc13db942e86014ea648ce5561359ae',
           '16Uiu2HAmRmAH3A9PzaAu2aQGxEoAyNZcT6bf7XZCJN8sSTsdcf3Q': '3b1a3813d357748b0eda09a3cabf2713e786965b6cafa0485fb0555ea6c3c34c',
           '16Uiu2HAmS8M32FEC14nFnc8uQL4CrvQ2rQKL1Txd3YQqXnSUu6sX': '8cc1e5985a9d320a15095a80ff49be31c8c71785ec2e9843690e12cc514dee44',
           '16Uiu2HAmSB4u2eQUsRxDB7pYeRPGZzV34AevoCZjebXgzAaBCDri': 'e676d36dbdefd36af141d759d68517f3ee1451922e243e136aa0556054d0bf0f',
           '16Uiu2HAmSE5uo7mR8XDaBePXVsmHXtUzyLAri5edYAYUQHXUebCQ': '788fb2c98605e6e2dd333c103aeeedbbc95882e8a961c292026cf2c4975449b9',
           '16Uiu2HAmSPyQ31zAUr1RY1L8ReeqqWnUjSyqpw7qm6RxRwbyYtG5': '16f7c08da9891d048c06e42532ab8f8f1783dec2e8926223a62580afd0d01d07',
           '16Uiu2HAmSZBxoLD38xzFP7eNuSqSqX3YkBaT9dtnsi4KkP25cS1f': 'b4fb22a663dcab68f9e365d99dad9f166b1053ba49c73d7a5e58df1cc3d64458',
           '16Uiu2HAmT4thh6szCCDRQNCcd9FHt8TricoGSJqK4DuJiN1xJhAF': '79b0b4405957aef64381bbbff4e24c4af19c4d11b8cd724d7877391079b5a36c',
           '16Uiu2HAmT8KUGvMMN9HLhvGdADo4NqHeQ6hKFaMDeyuWLa2LS3xR': '0e10214f3c0d83c25ebcc0555587c4b6ddea55d9e82ac407439aebca5e2b6d80',
           '16Uiu2HAmTCua75sDufxd9LVRXYwomPUu3ER5RxQnBFjK1Z43YWVX': '891e49ffd33bf71ba264d9e2585804585b06ac9a26d51514dfbcf6104ada328c',
           '16Uiu2HAmTmSV31nPuNYRNDeUaq1k8gtKSU3aYdC4JonMbVHXQVtx': 'afb83d79b91cccd806cb8bbfe609a6f92f2fcd51c91215404143725eb9237f12',
           '16Uiu2HAmUA6dPNUdhg3HCmupjFZC7nPZJzPnxBm6HpEqUhXiH44n': 'd0e1e9f6230b44b3c6743b6dbc68491686ca9c3c2fa73ddbeea3408d9be63a10',
           '16Uiu2HAmUmWFsajcKnHK4tRdfF64ku4DhCpx7NojQvYmiR5MvrfN': 'e8e59b7a64da0ba4baa854e2647ee2a2a8fa184dfc3c3709fa7abc126ab517fe',
           '16Uiu2HAmVa4q41eVbYAa3vSc4mbJx4S6SQaGL8XsDNk7BwNEE1J4': 'ae83e1dd1d0a3a0bbaa1c1c1e19b62586945f820c946f3b810e3177706fa27fc',
           '16Uiu2HAmVbCLUPHdfYxn3d3vLoHtNZgaJm9M7P77NXU2ZjcZ9e9p': 'dc54615271a4daae4477bfb2c8836bb6242b98c717ef2967d02c769e65b99683',
           '16Uiu2HAmVjoo3kk8exCALSSmBkgXGb6sfZ7rKpXVUgzstFNoPDLF': '755a76071fc590b893640e7d77ce0a4816258f307d5157a23abf64cdc0347349',
           '16Uiu2HAmVmERPFurWrpjqdFzmJc3CN2zz2stDjkqQ56EV1bZFGh5': '9a4af2e7acf17259e1ca50c3e6ecffc110ef63fe64f41d6802b9007e0c4c5d50',
           '16Uiu2HAmVrnDKphoVtGM7TK4YSt7MsJCsddocMD1gdWdUL4DwNwf': '0714d00d4a6e07eac3eae39addca4757a163a051e0c81e8f2b35b2a16297ab7c'}
