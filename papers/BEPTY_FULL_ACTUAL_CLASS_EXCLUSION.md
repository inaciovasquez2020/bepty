# BEpTy Full Actual-Class Exclusion

For the tested pair
\[
(A,B)=(G_{\mathrm{prism}},G_{K_{3,3}}),
\]
implemented by `regular_equal_cc_pair()`, the current actual compared executable class
\[
\mathcal R_{\mathrm{URF,actual}}=\{\#V,\#E,L_{\deg},I_{\mathrm{cc}}\}
\]
does not separate the pair:
\[
\#V(A)=\#V(B),\qquad \#E(A)=\#E(B),\qquad L_{\deg}(A)=L_{\deg}(B),\qquad I_{\mathrm{cc}}(A,B)=0.
\]

However the BEpTy valuation
\[
\beta_{\triangle}(A,B)=\triangle(B)-\triangle(A)
\]
does separate:
\[
\triangle(G_{\mathrm{prism}})=2,\qquad \triangle(G_{K_{3,3}})=0,
\]
hence
\[
\beta_{\triangle}(G_{\mathrm{prism}},G_{K_{3,3}})=-2\neq 0.
\]

Therefore BEpTy has a tested separating capability not furnished by the current actual compared executable class.
