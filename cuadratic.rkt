;; cuadratic :: Number Number Number -> Number
;; calcula el valor ax^2+b
(define (cuadratic x a b)
    (+ (* a (square x) b)))