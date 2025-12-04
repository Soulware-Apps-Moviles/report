<h4 id="development-evidence-for-sprint-review-2">Development Evidence for Sprint Review</h4>

En este segundo sprint, se ha cubierto la deuda técnica dejada en el sprint anterior, incluyendo alcances como la landing page del producto.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commit on |
| - | - | - | - | - | - |
| landing-page | hotfix/hero-section | 160dc9b747fb8fbc0e99a608e1adde6a4259b593 | chore: add customer app (Kotlin App) version download link | | 12/11/2025 |
| landing-page | hotfix/hero-section | 451a387ed83d5057e0429b1e1fe128d141306018 | refactor: move version swap button functionality into navbar as an item | | 12/11/2025 |
| landing-page | release/1.0.0 | 3abe89997b7777bbd366715c18855296ffe6c32e | chore: add README.md | hopefully SOMEONE bothers to read it... | 12/11/2025 |
| landing-page | release/1.0.0 | 3da537a6f93c297705d7498d3040382f9dc4e40f | feat: add auto redirect from root into 'en/customersÂ' as fallback | | 12/11/2025 |
| landing-page | feature/terms | ba870c1e1e9ba803de40aa84d25d2986aaea8c08 | feat: add terms and conditions page | (bis) | 12/11/2025 |
| landing-page | feature/privacy | 7e94e1831049a5a12574ea10f083b34862fadebe | feat: add privacy policy page | I had to tweak so many things because I didn't make my components assuming we would have these sections. | 12/11/2025 |
| landing-page | bugfix/hero-section | 59899df24ba11ffee3866a6c9ccace02af75d437 | refactor: change the name of the landing page layout component | | 12/11/2025 |
| landing-page | bugfix/hero-section | 316808ec2b9aa10dac25ab24dc4c8623aa6fae8c | fix: amend intermediate breakpoint on hero section | | 12/11/2025 |
| landing-page | feature/footer | 982d3e1d7859fe572240b68f4a4d5324e43824dd | feat: add footer section | | 12/11/2025 |
| landing-page | feature/reviews | d0af2c6ee161a13005c4833198a60505f109d376 | fix: amend wrongful headers for new section | | 12/11/2025 |
| landing-page | feature/reviews | 8912cef4fe179fe0a0e269174e19223ec1a78d94 | feat: add reviews section | also amended some kind of fixated padding I think suits well for all sections | 12/11/2025 |
| landing-page | feature/features-section | c7ffccf4ce1b01723f65be83aecc42c3b61ae87f | fix: amend mobile view breakpoints | had to add an intermediate view for tablets... kind off. Rather, I added md: conditional tailwind classes that make the transition softer. Im pretty sure I also touched a little bit of the components font sizes because they werent as readable as I expected them to be | 11/11/2025 |
| landing-page | feature/features-section | 92e48eacbd8f740ddfeaf6e816da0eb4c55d4568 | fix: amend missleading header 'features' for 'es' locale | | 11/11/2025 |
| landing-page | feature/features-section | df90332636f83ed6c67878abba474fbb08d7655c | feat: add feature section | there was also a bug that didnt allow tablet (md breakpoint) to show the mobile nav menu toggle | 11/11/2025 |
| landing-page | feature/hero-section | a876d6bc30208d5d4253e541ad738aff03640c78 | feat: add hero section for customers and stores | | 10/11/2025 |
| landing-page | feature/layout | 3b2c304dd0850ebdf664e40679aa0f9858080f1d | feat: add i18n support | as a test, tried it on generating both user visible content and non-visible data such as metadata. This commit also includes routing fallback to test if next-intl pathnames config was working as intended. In consequence, this commit is probably unnecesarily big | 09/11/2025 |
| landing-page | main | 5284c0b33573e07f20c8bc68f367745a7b3b3509 | chore: initial commit | | 09/11/2025 |
| kotlin-app | feature/myshop | 73854d51a5985688a124d08bdf87c7ff9b4deddd | feat:add shop-staff | | 03/11/2025 |
| kotlin-app | feature/myshop | a99bee6befcfdd831fb54c0e318df587263a12ea | feat(auth): Implementa flujo de Auth y Staff con conexión a backend | | 08/11/2025 |
| kotlin-app | feature/myshop | 6d14defe00db88c128d96365017be315b4e6bb3d |feat: Implementa flujo de Auth y Staffcompleto con UI y conexión | | 13/11/2025 |
| kotlin-app | feature/myshop | 2a41018959712e9b249f3cdf519235ca285ade6c |fix:abdate login | | 13/11/2025 |
| kotlin-app | feature/orders | 69e0eed63ce1190614bd4ff48a51ecbdb33c244d |feat: add orders | | 7/11/2025 |
| kotlin-app | feature/orders | fb2af08a1ad77cc967f0721ed3f9693779727fbc |feat: add orders design and navigation | | 12/11/2025 |
| kotlin-app | feature/orders | 83075fb8ce0d66ea54ea8a387445c08f8104f620 |feat: add room | | 12/11/2025 |
| kotlin-app | feature/finances | c47fa37dcb6868c760768659a33c26a1c8f10bea |feat: add finances | | 12/11/2025 |
| kotlin-app | feature/finances | 303da6b315d99f8be14f1383071491d188bca807 |feat: add room | | 13/11/2025 |
| kotlin-app | develop | 6587925dd190ce6d1482bd3f38bdebe4d86dc308 |Fix merging conflicts | | 13/11/2025 |
| kotlin-app | develop | 04434c496959d61492eb80893704151f76d586e0 |fix: fix duplicated remote modules | | 13/11/2025 |
| kotlin-app | develop | 50311cfac0315205a86e9ad74fd62a2dbda7395d |fix: api call | | 13/11/2025 |
| kotlin-app | develop | 2af38d008d46b5048dca4620f33c75748d2c3586 |fiz: fix inventory feature | | 13/11/2025 |
| kotlin-app | develop | 3a74d9805cb1c828bb97d14c04b357cda317feb1 |feat: add new token | | 13/11/2025 |
| tcompro | develop | 0d7de54867b0d240e4428a0b7eb151b0a6f8c923 |feat: add update credit limit of a trusted customer endpoint | | 21/10/2025 |
| tcompro | develop | d8ee7fc724eefe02106ced880cc9f3984031f6d8 |chore: add name and description to shop products | | 21/10/2025 |
| tcompro | develop | 94624b2d8c96bb627d2d32ee2825c65030b74994 |feat: add websocket connection with orders | | 24/10/2025 |
| tcompro | develop | df7eb80abf0534217feffae58c0334e1709bbea2 |chore: create a payment or debt after a order concluded | | 24/10/2025 |
| tcompro | develop | c662a3a6c3b85d71403e6435695f77625f24b295 |bugfix: fix flutter not connect with websocket because there was no endpoint with native websocket | | 25/10/2025 |
| tcompro | develop | d7c6b96f06d47ca39434339241e77e916bc3c5a6 |chore: remove shop id to create a profile | | 06/11/2025 |
| tcompro | develop | 8fea376bb5eb5dac4faad0793f792e437b57141f |feat: add get product catalog by name | | 06/11/2025 |
| tcompro | develop | 820e9f543faf16420f7080679c9c0378ad46a6fe |feat: add product catalog endpoint with filters | | 06/11/2025 |
| tcompro | develop | f71823def284bdb0a2d9417583df32b4b9e641c9 |chore: add image url to products | | 07/11/2025 |
| tcompro | develop | b20e3421097ad510a0e168daeae1887572b96314 |bugfix: remove favorite product is not using correct parameters | | 10/11/2025 |
| tcompro | develop | b34db1168c91c024e6ba5ad683a79e2e8dd71d9c |bugfix: fix data validation problems in hire shopkeeper endpoint | | 11/11/2025 |
| tcompro | develop | 113ee545763379aedda0550dc752e228ff4e0fd9 |bugfix: fix status name are always null in get debts endpoint with query params | | 13/11/2025 |
| tcompro | develop | ff1d7c33f73be27c4f03d19d0facd681e2f57fc0 |feat: add search by name in get all shopping lists endpoint | | 13/11/2025 |
| flutter-app | main | b921808142ac41343f8f002756ced4cd456dedba | feat: add favorites feature  | | 03/12/2025 |
| flutter-app | N/A | e9288904bf4ac1a0245a0974fe1c744aea3fc451 | refactor: prevent decreasing quantity on shopping bag when it is equal to 1 causing the item to be removed | not as fancy as sliding it to the side | 03/12/2025 |
| flutter-app | N/A | 503fe0151f169a0e3f71ba7e5cdebfc557306b27 | fix: amend product detail page not being able to add products to the shopping bag | | 03/12/2025 |
| flutter-app | N/A | 2f311dae6d67e46bf339c8eccfebe6794c0533a9 | chore: cleaning project | also found a missing interaction, may have to do this before the thing I was planning to since it is critical | 03/12/2025 |
| flutter-app | N/A | d3dacd38510756834ed0e914f489aee3ff04a30f | chore: removed unused favorites page (read long message) | the favorites feature was planned to be a view nested inside the 'you' feature. As such, it doesnt deserve its own folder. To add salt on the wound this wasnt even implemented on a real view widget, and I find no point on using it as a base to create one since I have the HomePage which already implements a lot of the logic and view I need. I also refactored the product card into the shared folder in anticipation to the incoming change | 03/12/2025 |
| flutter-app | N/A | a1a76bce210accebcaf3a23f92176d52e70d4563 | fix: amend visual style of you page  | | 03/12/2025 |
| flutter-app | N/A | ac8002ad5c0010e08b6815fd886a6b1c47e5072d | fix: amend visible application name for end user  | | 03/12/2025 |
| flutter-app | N/A | 85b9d28e371ca0a299a2ca673bf36d636e3f8d8f | fix: added missing permission for internet  | | 03/12/2025 |
| flutter-app | N/A | 0fe078370aefd945a4234c178debc35cfdf56efc | feat: add you page  | | 03/12/2025 |
| flutter-app | feature/shopping-bag | 88d3d5619245643300cfc981ab231a32769b2d66 | fix: minor bugfixes | wrongful colors, spanish labels, etc. | 03/12/2025 |
| flutter-app | N/A | 6d79495529114163712fafc1ea74131bde82526f | fix: amend request body being sent to order service on create order | | 03/12/2025 |
| flutter-app | N/A | 887dbee139a5e50036e706c5a015d04d79522cad | feat: add basic logic for order review page | its not working yet but this commit is way too long for me to feel comfortable making it bigger | 03/12/2025 |
| flutter-app | N/A | 6b7d446cbef862a0803b3483eef7b9f25bbddccd | refactor: change domain model to use product class inside of shopping list item | it was triggering me so much | 03/12/2025 |
| flutter-app | N/A | 385159e3a8f9030c982431202778a1a9f6f5e846 | chore: rename bag item into shopping bag item for consistency | | 03/12/2025 |
| flutter-app | N/A | d6f391ea9622baaa66c0892ca969ddf206845503 | chore: rename shopping item into shopping list item for consistency | | 03/12/2025 |
| flutter-app | N/A | 9b685a792bcefe10573f2e37fc10d3461fbd1e8d | fix: solve shopping lists not adding full quantity when adding the whole list to the bag | | 03/12/2025 |
| flutter-app | N/A | 281859aeedfc07f182eb6e574694243b9f0ebd67 | refactor: separate shopping list detail to have its own bloc | with plain values the UI wasnt reacting to interactions | 03/12/2025 |
| flutter-app | N/A | 3d8c88fbedf981f60c168db9c191936936d0548c | fix: amend visual and functional bugs  | | 03/12/2025 |
| flutter-app | N/A | b9e8ac5b4ac9dce5e9dca67ca046c688c9fd5b03 | chore: transport layer commit  | | 02/12/2025 |
| flutter-app | N/A | dcf3772eecdf9547e9a016736a6cbac1c2e8454d | chore: added more detail to placeholder  | | 02/12/2025 |
| flutter-app | N/A | 25bdbd6ca37352ec2bfebd909484fd7f1f3c4cfa | feat: add placeholder order review page | | 02/12/2025 |
| flutter-app | N/A | ab394e6a9fc8042a85580b24496788be0409f6c2 | chore: upgraded shop card format | | 02/12/2025 |
| flutter-app | N/A | 7ee7fa48b6d650421bd8d65bc87a53581714b504 | refactor: renamed components from store to shop for better overall consistency | | 02/12/2025 |
| flutter-app | N/A | f7f51bd4b40a2718783934ad0b92b13ce356bd69 | refactor: move shop card and bottom shop selection bar as independant components | | 02/12/2025 |
| flutter-app | N/A | 8325138bad0c39860e8b88310b2619a3a75acdd5 | feat: add store selection page | | 02/12/2025 |
| flutter-app | N/A | 47022f69bd47e09c31387697c2fa4fd9d37e50d4 | chore: minor code fixes | | 01/12/2025 |
| flutter-app | N/A | 491e2f61522ba43deee73149e07c2acd393c38b4 | feat: add placeholder select store page | | 01/12/2025 |
| flutter-app | N/A | 35111e81e13213a7c959d0a98881f2880b831095 | chore: removed unused import | | 01/12/2025 |
| flutter-app | N/A | 35f05c1eb896261363da9c0993dca6559ba735c9 | refactor: moved shopping list creation modal into a separate component | also made it more similar to the rest of the UI elements | 30/11/2025 |
| flutter-app | N/A | acfd821a49f39e1a517506b650a4f633bb2b3914 | feat: add from shopping list to bag feature | also fixed some code inconsistencies | 30/11/2025 |
| flutter-app | N/A | 5d0e7d9240952294a16476335864f395868109e9 | chore: upgraded shopping list card | | 30/11/2025 |
| flutter-app | N/A | b5eb38c7888daeaf1b6e209aa1409edd82abe063 | fix: fix shopping lists not syncing with events triggered by product details page | | 30/11/2025 |
| flutter-app | N/A | 4a46f5d111056b164d7a310eef6f926c6e6da18d | feat: implement add to shopping list feature | | 30/11/2025 |
| flutter-app | N/A | d553d68abc66bac7af0120e3925008966533565e | feat: add shopping bag page | | 30/11/2025 |
| flutter-app | N/A | 57c44ae3621c115a1c951cd082461e32d2784421 | chore: refactored favorite.dart into domain dir | | 30/11/2025 |
| flutter-app | N/A | 7ffe19619cd1eb0f99bd0afe1522e7df52cd19a6 | feat: add shopping bag data persistence and in memory global state | | 30/11/2025 |
| flutter-app | N/A | aa1b5c51ffe8d96aeae99510dbbb651cb5985540 | created local database for shopping bag | | 30/11/2025 |
| flutter-app | N/A | c8390f97b80422935b16af8348b93b4ee384e48d | chore: split shared data module to differentiate storage data and remote data | | 30/11/2025 |
| flutter-app | N/A | b3db50804cdcbaf73c1ef9c5ea4404836d51ffc2 | fix: add repository product stream and home bloc stream subscription to keep consistency when using toggle favorite on product details page | | 29/11/2025 |
| flutter-app | N/A | 6bc5bb61f590c77d14d36057297c7e5e1a442524 | fix: amend details page not being able to mark products as favorites | | 29/11/2025 |
| flutter-app | N/A | 2211bbd51ef25623831021c2a0dbf53f4e443014 | chore: remove unneded event for home page | | 29/11/2025 |
| flutter-app | N/A | 82922f0edd76a5142d9afaa0894162581c2567f8 | fix: fixed favorite feature | | 29/11/2025 |
| flutter-app | N/A | 8bacb3c32a19d2eab79905feef2f3662923637a4 | chore: change home events structure to carry user id | required for later on, as product repository should completely centralize the manipulation of products in general | 29/11/2025 |
| flutter-app | N/A | 22cb723e19407722357deb0d551c75297af5871a | refactor: transform product into a shared repository instead of a feature scoped service | | 29/11/2025 |
| flutter-app | N/A | 2891675d2619b8a2f92297c25b29ff6be45c836d | feat: add register feature | ensured the integration of the feature allows to instantly log in once the registration form was successful | 24/11/2025 |
| flutter-app | N/A | e7c648a6c75c6d127f8e0335d08704676d23c756 | feat: add login feature and a lot more (read long message) | so basically, I had to create a way to manage certain global values (token and user profile data). This was done by using Cubits. I also created an http interceptor and changed all services to work based on it, to sort of standarize the way we create services and prevent hard coding the reading of the Bearer token. Lastly, I coded the login feature. | 23/11/2025 | 