# HIGH_GIRTH_LOCAL_WEIGHTING_SEPARATION_GAP

Status: OPEN

## Gap

The candidate valuation

V_r(G) = \sum_{i=1}^{m} i * p_i(G)

separates the current witness instance but is not yet proved to separate all
distinct rooted radius-r profile vectors.

## Weakest Missing Object

Construct a universally valid canonical weight vector
w = (w_1, ..., w_m)
such that for all finite bounded-degree graphs G,H,

P_r(G) != P_r(H) => \sum_{i=1}^{m} w_i p_i(G) != \sum_{i=1}^{m} w_i p_i(H).

## Reduction

universal_weighting_separation => HIGH_GIRTH_LOCAL_VALUATION_LEMMA
