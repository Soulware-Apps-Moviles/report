<h4 id="development-evidence-for-sprint-review-2">Development Evidence for Sprint Review</h4>

En este segundo sprint, se ha cubierto la deuda técnica dejada en el sprint anterior, incluyendo alcances como la landing page del producto.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commit on |
| - | - | - | - | - | - |
| tcompro | hotfix/hero-section | 160dc9b747fb8fbc0e99a608e1adde6a4259b593 | chore: add customer app (Kotlin App) version download link | | 12/11/2025 |
| tcompro | hotfix/hero-section | 451a387ed83d5057e0429b1e1fe128d141306018 | refactor: move version swap button functionality into navbar as an item | | 12/11/2025 |
| tcompro | release/1.0.0 | 3abe89997b7777bbd366715c18855296ffe6c32e | chore: add README.md | hopefully SOMEONE bothers to read it... | 12/11/2025 |
| tcompro | release/1.0.0 | 3da537a6f93c297705d7498d3040382f9dc4e40f | feat: add auto redirect from root into 'en/customersÂ' as fallback |  | 12/11/2025 |
| tcompro | feature/terms | ba870c1e1e9ba803de40aa84d25d2986aaea8c08 | feat: add terms and conditions page | (bis) | 12/11/2025 |
| tcompro | feature/privacy | 7e94e1831049a5a12574ea10f083b34862fadebe | feat: add privacy policy page | I had to tweak so many things because I didn't make my components assuming we would have these sections. | 12/11/2025 |
| tcompro | bugfix/hero-section | 59899df24ba11ffee3866a6c9ccace02af75d437 | refactor: change the name of the landing page layout component |  | 12/11/2025 |
| tcompro | bugfix/hero-section | 316808ec2b9aa10dac25ab24dc4c8623aa6fae8c | fix: amend intermediate breakpoint on hero section |  | 12/11/2025 |
| tcompro | feature/footer | 982d3e1d7859fe572240b68f4a4d5324e43824dd | feat: add footer section |  | 12/11/2025 |
| tcompro | feature/reviews | d0af2c6ee161a13005c4833198a60505f109d376 | fix: amend wrongful headers for new section |  | 12/11/2025 |
| tcompro | feature/reviews | 8912cef4fe179fe0a0e269174e19223ec1a78d94 | feat: add reviews section | also amended some kind of fixated padding I think suits well for all sections | 12/11/2025 |
| tcompro | feature/features-section | c7ffccf4ce1b01723f65be83aecc42c3b61ae87f | fix: amend mobile view breakpoints | had to add an intermediate view for tablets... kind off. Rather, I added md: conditional tailwind classes that make the transition softer. Im pretty sure I also touched a little bit of the components font sizes because they werent as readable as I expected them to be | 11/11/2025 |
| tcompro | feature/features-section | 92e48eacbd8f740ddfeaf6e816da0eb4c55d4568 | fix: amend missleading header 'features' for 'es' locale |  | 11/11/2025 |
| tcompro | feature/features-section | df90332636f83ed6c67878abba474fbb08d7655c | feat: add feature section | there was also a bug that didnt allow tablet (md breakpoint) to show the mobile nav menu toggle | 11/11/2025 |
| tcompro | feature/hero-section | a876d6bc30208d5d4253e541ad738aff03640c78 | feat: add hero section for customers and stores | | 10/11/2025 |
| tcompro | feature/layout | 3b2c304dd0850ebdf664e40679aa0f9858080f1d | feat: add i18n support | as a test, tried it on generating both user visible content and non-visible data such as metadata. This commit also includes routing fallback to test if next-intl pathnames config was working as intended. In consequence, this commit is probably unnecesarily big | 09/11/2025 |
| tcompro | main | 5284c0b33573e07f20c8bc68f367745a7b3b3509 | chore: initial commit |  | 09/11/2025 |