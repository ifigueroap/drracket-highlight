;; solve-cuadratic-let :: Number Number Number -> Number
;; encuentra una solución real para ax^2+bx+c, si existe.
(define (solve-cuadratic-let a b c)
    (let ([discriminant (- (* b b) (* 4 a c))])
            (if (> discriminant 0)
                (+ (- b) (/ (sqrt discriminant) (* 2 a)))
                (error "No real solution"))))
    