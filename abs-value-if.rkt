;; abs-value-if :: Number -> Number
;; calcula el valor absoluto de x
(define (abs-value-if x)
    (if (>= x 0)
        x
        (- x)))