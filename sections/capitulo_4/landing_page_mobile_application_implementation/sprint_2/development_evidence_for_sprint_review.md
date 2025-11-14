<h4 id="development-evidence-for-sprint-review-2">Development Evidence for Sprint Review</h4>

En este segundo sprint, se ha cubierto la deuda técnica dejada en el sprint anterior, incluyendo alcances como la landing page del producto.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commit on |
| - | - | - | - | - | - |
| landing-page | hotfix/hero-section | 160dc9b747fb8fbc0e99a608e1adde6a4259b593 | chore: add customer app (Kotlin App) version download link | | 12/11/2025 |
| landing-page | hotfix/hero-section | 451a387ed83d5057e0429b1e1fe128d141306018 | refactor: move version swap button functionality into navbar as an item | | 12/11/2025 |
| landing-page | release/1.0.0 | 3abe89997b7777bbd366715c18855296ffe6c32e | chore: add README.md | hopefully SOMEONE bothers to read it... | 12/11/2025 |
| landing-page | release/1.0.0 | 3da537a6f93c297705d7498d3040382f9dc4e40f | feat: add auto redirect from root into 'en/customersÂ' as fallback |  | 12/11/2025 |
| landing-page | feature/terms | ba870c1e1e9ba803de40aa84d25d2986aaea8c08 | feat: add terms and conditions page | (bis) | 12/11/2025 |
| landing-page | feature/privacy | 7e94e1831049a5a12574ea10f083b34862fadebe | feat: add privacy policy page | I had to tweak so many things because I didn't make my components assuming we would have these sections. | 12/11/2025 |
| landing-page | bugfix/hero-section | 59899df24ba11ffee3866a6c9ccace02af75d437 | refactor: change the name of the landing page layout component |  | 12/11/2025 |
| landing-page | bugfix/hero-section | 316808ec2b9aa10dac25ab24dc4c8623aa6fae8c | fix: amend intermediate breakpoint on hero section |  | 12/11/2025 |
| landing-page | feature/footer | 982d3e1d7859fe572240b68f4a4d5324e43824dd | feat: add footer section |  | 12/11/2025 |
| landing-page | feature/reviews | d0af2c6ee161a13005c4833198a60505f109d376 | fix: amend wrongful headers for new section |  | 12/11/2025 |
| landing-page | feature/reviews | 8912cef4fe179fe0a0e269174e19223ec1a78d94 | feat: add reviews section | also amended some kind of fixated padding I think suits well for all sections | 12/11/2025 |
| landing-page | feature/features-section | c7ffccf4ce1b01723f65be83aecc42c3b61ae87f | fix: amend mobile view breakpoints | had to add an intermediate view for tablets... kind off. Rather, I added md: conditional tailwind classes that make the transition softer. Im pretty sure I also touched a little bit of the components font sizes because they werent as readable as I expected them to be | 11/11/2025 |
| landing-page | feature/features-section | 92e48eacbd8f740ddfeaf6e816da0eb4c55d4568 | fix: amend missleading header 'features' for 'es' locale |  | 11/11/2025 |
| landing-page | feature/features-section | df90332636f83ed6c67878abba474fbb08d7655c | feat: add feature section | there was also a bug that didnt allow tablet (md breakpoint) to show the mobile nav menu toggle | 11/11/2025 |
| landing-page | feature/hero-section | a876d6bc30208d5d4253e541ad738aff03640c78 | feat: add hero section for customers and stores | | 10/11/2025 |
| landing-page | feature/layout | 3b2c304dd0850ebdf664e40679aa0f9858080f1d | feat: add i18n support | as a test, tried it on generating both user visible content and non-visible data such as metadata. This commit also includes routing fallback to test if next-intl pathnames config was working as intended. In consequence, this commit is probably unnecesarily big | 09/11/2025 |
| landing-page | main | 5284c0b33573e07f20c8bc68f367745a7b3b3509 | chore: initial commit |  | 09/11/2025 |
| kotlin-app | feature/myshop | 73854d51a5985688a124d08bdf87c7ff9b4deddd | feat:add shop-staff |  | 03/11/2025 |
| kotlin-app | feature/myshop | a99bee6befcfdd831fb54c0e318df587263a12ea | feat(auth): Implementa flujo de Auth y Staff con conexión a backend |  | 08/11/2025 |
| kotlin-app | feature/myshop | 6d14defe00db88c128d96365017be315b4e6bb3d |feat: Implementa flujo de Auth y Staffcompleto con UI y conexión |  | 13/11/2025 |
| kotlin-app | feature/myshop | 2a41018959712e9b249f3cdf519235ca285ade6c |fix:abdate login |  | 13/11/2025 |
| kotlin-app | feature/orders | 69e0eed63ce1190614bd4ff48a51ecbdb33c244d |feat: add orders |  | 7/11/2025 |
| kotlin-app | feature/orders | fb2af08a1ad77cc967f0721ed3f9693779727fbc |feat: add orders design and navigation |  | 12/11/2025 |
| kotlin-app | feature/orders | 83075fb8ce0d66ea54ea8a387445c08f8104f620 |feat: add room |  | 12/11/2025 |
| kotlin-app | feature/finances | c47fa37dcb6868c760768659a33c26a1c8f10bea |feat: add finances |  | 12/11/2025 |
| kotlin-app | feature/finances | 303da6b315d99f8be14f1383071491d188bca807 |feat: add room |  | 13/11/2025 |
| kotlin-app | develop | 6587925dd190ce6d1482bd3f38bdebe4d86dc308 |Fix merging conflicts |  | 13/11/2025 |
| kotlin-app | develop | 04434c496959d61492eb80893704151f76d586e0 |fix: fix duplicated remote modules |  | 13/11/2025 |
| kotlin-app | develop | 50311cfac0315205a86e9ad74fd62a2dbda7395d |fix: api call |  | 13/11/2025 |
| kotlin-app | develop | 2af38d008d46b5048dca4620f33c75748d2c3586 |fiz: fix inventory feature |  | 13/11/2025 |
| kotlin-app | develop | 3a74d9805cb1c828bb97d14c04b357cda317feb1 |feat: add new token |  | 13/11/2025 |
| tcompro | develop | 0d7de54867b0d240e4428a0b7eb151b0a6f8c923 |feat: add update credit limit of a trusted customer endpoint |  | 21/10/2025 |
| tcompro | develop | d8ee7fc724eefe02106ced880cc9f3984031f6d8 |chore: add name and description to shop products |  | 21/10/2025 |
| tcompro | develop | 94624b2d8c96bb627d2d32ee2825c65030b74994 |feat: add websocket connection with orders |  | 24/10/2025 |
| tcompro | develop | df7eb80abf0534217feffae58c0334e1709bbea2 |chore: create a payment or debt after a order concluded |  | 24/10/2025 |
| tcompro | develop | c662a3a6c3b85d71403e6435695f77625f24b295 |bugfix: fix flutter not connect with websocket because there was no endpoint with native websocket |  | 25/10/2025 |
| tcompro | develop | d7c6b96f06d47ca39434339241e77e916bc3c5a6 |chore: remove shop id to create a profile |  | 06/11/2025 |
| tcompro | develop | 8fea376bb5eb5dac4faad0793f792e437b57141f |feat: add get product catalog by name |  | 06/11/2025 |
| tcompro | develop | 820e9f543faf16420f7080679c9c0378ad46a6fe |feat: add product catalog endpoint with filters |  | 06/11/2025 |
| tcompro | develop | f71823def284bdb0a2d9417583df32b4b9e641c9 |chore: add image url to products |  | 07/11/2025 |
| tcompro | develop | b20e3421097ad510a0e168daeae1887572b96314 |bugfix: remove favorite product is not using correct parameters |  | 10/11/2025 |
| tcompro | develop | b34db1168c91c024e6ba5ad683a79e2e8dd71d9c |bugfix: fix data validation problems in hire shopkeeper endpoint |  | 11/11/2025 |
| tcompro | develop | 113ee545763379aedda0550dc752e228ff4e0fd9 |bugfix: fix status name are always null in get debts endpoint with query params |  | 13/11/2025 |
| tcompro | develop | ff1d7c33f73be27c4f03d19d0facd681e2f57fc0 |feat: add search by name in get all shopping lists endpoint |  | 13/11/2025 |
| flutter-app | main | 0c6a57e3cd2d80b9fd88c49fa499bbd9615b2e62 |first commit |  | 06/11/2025 |
| flutter-app | main | 1cd04cbf31420b342f341f596a954e2234a66036 |chore: setup project |  | 06/11/2025 |
| flutter-app | develop | 8eb31b3140e3c6919a57fe110c695ccac4552b77 |chore: setup security config |  | 06/11/2025 |
| flutter-app | develop | 4a6ccd9d2e7db6fe2aef9756e5fa400965b563c6 |feat: add fetch all products by name or category feature |  | 06/11/2025 |
| flutter-app | feature/home | 4a6ccd9d2e7db6fe2aef9756e5fa400965b563c6 |feat: add fetch all products by name or category feature |  | 06/11/2025 |
| flutter-app | feature/home | 78b1032d43060117ee90f9e9bc31b8cd3418f295 |bugfix: product card is not using image url |  | 07/11/2025 |
| flutter-app | feature/home | 3a536d6834fb655f5538df9f0c964b53e1a4198b |feat: add product detail page |  | 07/11/2025 |
| flutter-app | feature/favorites | d8b0ae34439196475875276d4469031b02b4dd37 |feat: add favorites feature in home and product detail |  | 10/11/2025 |
| flutter-app | feature/favorites | 3a92641a01375b0161ec556790b11c4754b8d3b0 |chore: change favorite button to feature/favorites widgets |  | 10/11/2025 |
| flutter-app | feature/shopping-lists | 592367a6eeaef9062ad777d95e27dddab485638f |feat: add fetch shopping lists page |  | 11/11/2025 |
| flutter-app | feature/shopping-lists | 2cfa401e69c0156db898e731485d7f66404613e5 |feat: add create a shopping list feature |  | 11/11/2025 |
| flutter-app | feature/shopping-lists | bd669ad7c08361495ebe0304cb72b44f73ff147f |feat: add search shopping list feature |  | 13/11/2025 |
| flutter-app | feature/shopping-lists | bd669ad7c08361495ebe0304cb72b44f73ff147f |feat: add search shopping list feature |  | 13/11/2025 |
| flutter-app | feature/shopping-lists | 5f4abc945fa6fdaf7584d9b099019d22030ad1cf |feat: add shopping list detail feature |  | 13/11/2025 |
| flutter-app | feature/shopping-lists | c3d5e3138f8436fb34c03bfa86e928a6989e07c0 |chore: add new colors to shopping list card and items |  | 13/11/2025 |
| flutter-app | feature/shopping-lists | 34410fcfb88f3438da88bd7bf422282b8d8969f5 |refactor: add shopping list is a modal now |  | 13/11/2025 |
| flutter-app | develop | e68cfbe7d0bd1a798ddc390d1f758306908abf85 |chore: configured supabase connection | it requires environment variables, check the supabase docs for flutter if you experience any problems | 13/11/2025 |
| flutter-app | feature/shopping-lists | 3047c7054901ec767de20729b18c34727f8ca791 |chore: add app icon |  | 13/11/2025 |